from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework.exceptions import AuthenticationFailed # Validación de Token (sin expirar)
import jwt, datetime, base64 # Manejo del token
from .serializers import ClienteJuridicoSerializer, ClienteNaturalSerializer, ClienteSerializer, DireccionSerializer, UsuarioSerializer # Serializadores
from .models import Cliente, ClienteJuridico, ClienteNatural, Direccion, Usuario # Modelos

# Create your views here.
class getToken(APIView):
    def post(self, request):
        headers = request.headers
        if 'Basic' not in headers:
            raise AuthenticationFailed('Envía un token!')
            
        basicTokenEncrypt = headers['Basic']
        usua_login = base64.b64decode(basicTokenEncrypt)
        usua_login = usua_login.decode()

        usuario = Usuario.objects.using('seguridad').filter(USUA_LOGIN=usua_login).first()

        if usuario is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        payload = {
            'id': usuario.USUA_LOGIN,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'tfhc-pc-pydj-bkd-mssql', algorithm = 'HS256')

        response = Response()

        response.data = {
            'jwt': token
        }

        return response

class validate(APIView):
    def post(self, request):
        headers = request.headers
        if 'Bearer' not in headers:
            raise AuthenticationFailed('Envía un token!')

        token = headers['Bearer']

        if not token:
            raise AuthenticationFailed('Envía un token!')

        try:
            payload = jwt.decode(token, 'tfhc-pc-pydj-bkd-mssql', algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token exporó!')

        usuario = Usuario.objects.using('seguridad').filter(USUA_LOGIN=payload['id']).first()
        
        if usuario is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        usuarioSerializer = UsuarioSerializer(usuario)

        userDict = usuarioSerializer.data

        del userDict['USUA_CLAVE']
        return Response(userDict)

def authenticate(request):
    headers = request.headers
    if 'Bearer' not in headers:
        return {"status": False, "message": "Envía un token!"}

    token = headers['Bearer']

    if not token:
        return {"status": False, "message": "Envía un token!"}
    try:
        payload = jwt.decode(token, 'tfhc-pc-pydj-bkd-mssql', algorithms = ['HS256'])
    except jwt.ExpiredSignatureError:
        return {"status": False, "message": "Token expiró!"}

    usuario = Usuario.objects.using('seguridad').filter(USUA_LOGIN=payload['id']).first()
    
    if usuario is None:
        return {"status": False, "message": "No se encontró usuario!"}
    
    usuarioSerializer = UsuarioSerializer(usuario)

    userDict = usuarioSerializer.data

    del userDict['USUA_CLAVE']
    return {"status": True, "message": "Autenticación exitosa!", "Usuario": userDict}

class cliente(APIView):
    def get(self, request):
        auth = authenticate(request)
        if auth['status'] is False:
            return Response(auth)

        data = request.GET
        cedula = data['cedula']
        
        cliente = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = cedula).first()
        clienteSerializer = ClienteSerializer(cliente)
        clienteDireccion = Direccion.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).first()
        clienteDireccionSerializer = DireccionSerializer(clienteDireccion)
        if cliente is None:
            return Response({"status": False, "message": "Cliente no encotrado"})
        
        if cliente.TICL_CODIGO.TICL_CODIGO == "N":
            cliente_detail = ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).first()
            clienteDetaillSerialize = ClienteNaturalSerializer(cliente_detail)
        if cliente.TICL_CODIGO.TICL_CODIGO == "J":
            cliente_detail = ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).first()
            clienteDetaillSerialize = ClienteJuridicoSerializer(cliente_detail)

        clienteData = clienteSerializer.data
        clienteData['detail'] = clienteDetaillSerialize.data
        clienteData['address'] = clienteDireccionSerializer.data

        return Response(
            {
                "status": True, 
                "message": "Exitoso", 
                "data": clienteData
            })
    
    def post(self, request): # Guardar Cliente:
        # Inicio Autenticar
        auth = authenticate(request)
        if auth['status'] is False:
            return Response(auth)
        # Fin Autenticar

        # Inicio Reservar información a manejar a partir del Request
        clienteData = request.data['cliente']
        clienteDetail = request.data['detail']
        clienteAddress = request.data['address']
        ticl_codigo = clienteData['TICL_CODIGO']
        tido_codigo = clienteData['TIDO_CODIGO']
        clie_identificacion = clienteData['CLIE_IDENTIFICACION']
        # Fin Reservar

        # Inicio Validar-Cliente
        # 1. Si ya existe
        # 2. Si ya existe pero tiene nueva dirección
        # 3. Si el tipo de cliente es válido
        # 4. Si el documento corresponde al tipo de cliente
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = clie_identificacion).first()

        if clienteChecking:
            addressChecking = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clienteChecking.CLIE_CODIGO, DIRE_DESCRIPCION = clienteAddress["DIRE_DESCRIPCION"])
            if addressChecking:
                return Response(f"Cliente {clie_identificacion} ya existe. Pasando a crédito...")
            return Response(f"Cliente {clie_identificacion} ya existe, pero viene nueva dirección {clienteAddress}. Actualizando...")

        if ticl_codigo == 'N':
            if tido_codigo == 'C' or tido_codigo == 'P':
                clienteSave = ClienteSerializer(data = clienteData)
                clienteSave.is_valid(raise_exception = True)
                return Response(clienteSave.data)
                if clienteSave.save():
                    return Response(f"Cliente guardado con el CLIE_CODIGO: {clienteSave.CLIE_CODIGO}")
                #clienteSerializer.save(using = 'clientes')
                # Guardar Dirección:
                return Response(f"Cliente tipo ({ticl_codigo})Natural")
            return Response(f"Cliente tipo Natural pero documentación incorrecta, se espera (C)Cédula o (P)Pasaporte y se recibió {tido_codigo}")

        if ticl_codigo == 'J':
            if tido_codigo == 'R':
                return Response(f"Cliente tipo ({ticl_codigo})Jurídico")
            return Response(f"Cliente tipo Jurídico pero documentación incorrecta, se espera (R)RUC y se recibió {tido_codigo}")

        #Fin Validar-Cliente
        
        # Inicio Respuesta
        return Response(f"Cliente tipo Invalido, se esperaba (N)Natural o (J)Juridico y se recibió {ticl_codigo}")

class Direccion(APIView):
    def get(self, request):
        return Response()