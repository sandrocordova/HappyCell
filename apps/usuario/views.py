from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework.exceptions import AuthenticationFailed # Validación de Token (sin expirar)
from rest_framework import status # Manejo de Status
import jwt, datetime, base64
from apps.apihc.serializers import UsuarioSerializer
from apps.agencia.models import UsuarioInfo, UsuarioMenu
from apps.agencia.api.serializer import UsuarioInfoSerializer, UsuarioMenuSerializer
from apps.apihc.models import Usuario
from django.shortcuts import render

# Create your views here.

# Create your views here.
class getToken(APIView):
    def post(self, request):
        headers = request.headers
        if 'User' not in headers:
            raise AuthenticationFailed({'status': status.HTTP_400_BAD_REQUEST,'message':'¡Envía un Usuario!'})
        if 'Password' not in headers:
            raise AuthenticationFailed({'status': status.HTTP_400_BAD_REQUEST,'message':'¡Envía una Contraseña!'})
            
        basicTokenEncrypt = headers['User']
        passwordEncrypt = headers['Password']
        usua_login = base64.b64decode(basicTokenEncrypt)
        usua_login = usua_login.decode()
        password_login = base64.b64decode(passwordEncrypt)
        password_login = password_login.decode()

        usuario = Usuario.objects.filter(USUA_LOGIN=usua_login).first()

        if usuario is None:
            raise AuthenticationFailed({'status': status.HTTP_400_BAD_REQUEST,'message':'Usuario no encontrado'})
        
        if not usuario.USUA_CLAVE.__eq__(password_login):
            raise AuthenticationFailed({'status': status.HTTP_400_BAD_REQUEST,'message':'Contraseña incorrecta'})
        
        payload = {
            'id': usuario.USUA_LOGIN,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            'iat': datetime.datetime.utcnow()
        }  

        token = jwt.encode(payload, 'tfhc-pc-pydj-bkd-mssql', algorithm = 'HS256')
        response = Response()

        message = ""
        user = usuario.USUA_CODIGO
        usuario = UsuarioInfo.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='"+user+"' and ms.MOSI_CODIGO= 1")
        if usuario:
            userOpciones = UsuarioMenu.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION, ve.vent_ventana FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO= tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO = om.MOSI_CODIGO inner join perfil_ventana pf on (om.opme_codigo = pf.OPME_CODIGO) inner join ventana ve ON (PF.VENT_CODIGO=VE.VENT_CODIGO and vent_ventana like '/%%') WHERE u.USUA_CODIGO = '"+user+"' and um.MOSI_CODIGO in (4,8,10) AND OM.OPME_CODIGO >= 800 order by om.opme_orden")  
            if userOpciones:
                serializerUsuarioMenu = UsuarioMenuSerializer(userOpciones, many = True)
                serializerUsuarioInfo = UsuarioInfoSerializer(usuario, many = True)
                opmeDescripcion = []
                menuPadre = []
                menuHijo = []
                for i in serializerUsuarioMenu.data:
                    menuHijo.append(
                                {
                                    "opme_descripcion":i["opme_descripcion"],
                                    "vent_descripcion": i["vent_descripcion"],
                                    "vent_ventana": i["vent_ventana"],
                                    })
                for i in serializerUsuarioMenu.data:
                    if i["opme_descripcion"] not in opmeDescripcion:
                        opmeDescripcion.append(i["opme_descripcion"])
                        menuPadre.append(
                                {
                                    "opme_descripcion":i["opme_descripcion"],
                                    "opme_orden": i["opme_orden"],
                                    "opme_codigo": i["opme_codigo"],
                                    "child": obtener_hijos(i["opme_descripcion"],menuHijo),
                                    })
                json_response = [
                                {
                                    "user_profile":serializerUsuarioInfo.data,
                                    "menu_access": menuPadre,
                                }
                            ]
                    
                response.data = {
                        'jwt': token,
                        'status': status.HTTP_200_OK,
                        'message': "Respuesta exitosa",
                        'data': json_response
                    }
                return response
            else: message =  "El usuario no tiene acceso a menús"
        else: message = "Rol de usuario no encontrado"

        response.data = {
            'jwt': token,
            'status': status.HTTP_200_OK,
            'message': message
        }

        return response

def obtener_hijos(opmeDescripcion, menuHijos):
    hijosReturn = []
    for hijo in menuHijos:
        if hijo["opme_descripcion"]==opmeDescripcion:
            hijosReturn.append(hijo)
    return hijosReturn

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
            raise AuthenticationFailed('Token expiró!')

        usuario = Usuario.objects.filter(USUA_LOGIN=payload['id']).first()
        if usuario is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        usuarioSerializer = UsuarioSerializer(usuario)

        userDict = usuarioSerializer.data

        del userDict['USUA_CLAVE']
        return Response(userDict)

def authenticate(request):
    headers = request.headers
    if 'Bearer' not in headers:
        return {"status": status.HTTP_401_UNAUTHORIZED, "message": "Envía un token!"}

    token = headers['Bearer']

    if not token:
        return {"status": status.HTTP_401_UNAUTHORIZED, "message": "Envía un token!"}
    try:
        payload = jwt.decode(token, 'tfhc-pc-pydj-bkd-mssql', algorithms = ['HS256'])
    except jwt.ExpiredSignatureError:
        return {"status": status.HTTP_401_UNAUTHORIZED, "message": "Token expiró!"}

    usuario = Usuario.objects.filter(USUA_LOGIN=payload['id']).first()
    
    if usuario is None:
        return {"status": status.HTTP_204_NO_CONTENT, "message": "No se encontró usuario!"}
    
    usuarioSerializer = UsuarioSerializer(usuario)

    userDict = usuarioSerializer.data

    del userDict['USUA_CLAVE']
    return {"status": status.HTTP_200_OK, "message": "Autenticación exitosa!", "Usuario": userDict}
