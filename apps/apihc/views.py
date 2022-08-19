from datetime import date, datetime
from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework.exceptions import AuthenticationFailed # Validación de Token (sin expirar)
from rest_framework import status # Manejo de Status
import jwt, datetime, base64
from .functions import actualizarCliente, actualizarClienteJuridico, actualizarClienteNatural, guardarAsesorCliente, validarAsesorExiste, validarCliente, validarClienteNatural, validarClienteJuridico, validarDireccion, validarTelefono, validarAsesor, validarObservacion, validarCuenta, validarVinculo, guardarCliente, guardarClienteNatural, guardarClienteJuridico, guardarDireccion, guardarTelefono, guardarAsesor, guardarObservacion, guardarCuentaBancaria, guardarVinculo # Manejo del token
from .serializers import ClienteJuridicoSerializer, ClienteNaturalSerializer, ClienteSerializer, DireccionSerializer, EstadoCivilSerializer, NacionalidadSerializer, NivelInstruccionSerializer, ProfesionSerializer, SituacionLaboralSerializer, TelefonoSerializer, TipoClienteSerializer, TipoDocumentoSerializer, UsuarioSerializer, ViviendaSerializer, ActividadEconomicaSerializer # Serializadores
from .models import Agencia, Asesor, Banco, Canton, Ciudad, Cliente, ClienteAsesor, ClienteJuridico, ClienteNatural, CuentaBancariaCliente, Direccion, Empresa, EstadoCivil, GrupoEconomico, Nacionalidad, NivelInstruccion, Observacion, Pais, Parroquia, Profesion, Provincia, Secuencia, Sexo, SituacionLaboral, Telefono, TipoAsesor, TipoBanca, TipoCliente, TipoCuenta, TipoDireccion, TipoDocumento, TipoEmpresa, TipoObservacion, TipoProyecto, TipoRol, TipoTelefono, TipoVinculo, Usuario, Vinculo, Vivienda, Zona, ActividadEconomica # Modelos

# Create your views here.
class getToken(APIView):
    def post(self, request):
        headers = request.headers
        if 'Basic' not in headers:
            raise AuthenticationFailed('Envía un token!')
            
        basicTokenEncrypt = headers['Basic']
        usua_login = base64.b64decode(basicTokenEncrypt)
        usua_login = usua_login.decode()

        usuario = Usuario.objects.filter(USUA_LOGIN=usua_login).first()

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

class CLIENTESView(APIView):
    def get(self, request):
        auth = authenticate(request)
        if auth['status'] != 200:
            return Response(auth)

        data = request.GET
        cedula = data['cedula']

        direcciones = {}
        
        cliente = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = cedula).first()
        clie_codigo = cliente.CLIE_CODIGO
        clienteSerializer = ClienteSerializer(cliente)
        clienteDirecciones = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).all()
        for clienteDireccion in clienteDirecciones:
            telefonos = {}
            clienteDireccionSerializer = DireccionSerializer(clienteDireccion)
            clienteDireccionTelefonos = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, DIRE_CODIGO = clienteDireccion.DIRE_CODIGO).all()
            for clienteDireccionTelefono in clienteDireccionTelefonos:
                clienteTelefonoSerializer = TelefonoSerializer(clienteDireccionTelefono)
                telefonos[int(clienteDireccionTelefono.TELE_CODIGO)] = clienteTelefonoSerializer.data
            direcciones[int(clienteDireccion.DIRE_CODIGO)] = clienteDireccionSerializer.data
            direcciones[int(clienteDireccion.DIRE_CODIGO)]['telefonos'] = telefonos

        clienteDireccionSerializer = DireccionSerializer(clienteDireccion)
        clienteTelefono = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        clienteTelefonoSerializer = TelefonoSerializer(clienteTelefono)
        if cliente is None:
            return Response({"status": status.HTTP_200_OK, "message": "Cliente no encotrado"})
        
        if cliente.TICL_CODIGO == "N":
            cliente_detail = ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).first()
            clienteDetaillSerialize = ClienteNaturalSerializer(cliente_detail)
        if cliente.TICL_CODIGO == "J":
            cliente_detail = ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = cliente.CLIE_CODIGO).first()
            clienteDetaillSerialize = ClienteJuridicoSerializer(cliente_detail)

        clienteDict = clienteSerializer.data
        clienteDict['NACI_CODIGO'] = NacionalidadSerializer(Nacionalidad.objects.using('clientes').filter(NACI_CODIGO = clienteDict['NACI_CODIGO']).first()).data
        clienteDict['ACTI_CODIGO'] = ActividadEconomicaSerializer(ActividadEconomica.objects.using('clientes').filter(ACTI_CODIGO = clienteDict['ACTI_CODIGO']).first()).data
        clienteDetailDict = clienteDetaillSerialize.data
        clienteDetailDict['PROF_CODIGO'] = ProfesionSerializer(Profesion.objects.using('clientes').filter(PROF_CODIGO = clienteDetailDict['PROF_CODIGO']).first()).data
        clienteDetailDict['NIIN_CODIGO'] = NivelInstruccionSerializer(NivelInstruccion.objects.using('clientes').filter(NIIN_CODIGO = clienteDetailDict['NIIN_CODIGO']).first()).data
        clienteDetailDict['ESCI_CODIGO'] = EstadoCivilSerializer(EstadoCivil.objects.using('clientes').filter(ESCI_CODIGO = clienteDetailDict['ESCI_CODIGO']).first()).data
        clienteDetailDict['CLIE_TIPO_VIVIENDA'] = ViviendaSerializer(Vivienda.objects.using('clientes').filter(VIVI_CODIGO = clienteDetailDict['CLIE_TIPO_VIVIENDA']).first()).data
        clienteDetailDict['CLIE_SITUACION_LABORAL'] = SituacionLaboralSerializer(SituacionLaboral.objects.using('clientes').filter(SITL_CODIGO = clienteDetailDict['CLIE_SITUACION_LABORAL']).first()).data

        clienteData = clienteDict
        clienteData['detalle'] = clienteDetailDict
        clienteData['direcciones'] = direcciones

        return Response(
            {
                "status": True, 
                "message": "Exitoso", 
                "data": clienteData
            })

    def post(self, request): # Guardar Cliente:
        # Inicio Autenticar
        auth = authenticate(request)
        if auth['status'] is not status.HTTP_200_OK:
            return Response(auth)
        # Fin Autenticar

        # Inicio Reservar información a manejar de Cliente a partir del REQUEST
        log = {}
        logIndex = 0

        data = request.data
        if 'cliente' in data:
            informacionCliente = data['cliente']
        else:
            informacionCliente = {}

        if 'detalle' in data:
            detallesCliente = data['detalle']
        else:
            detallesCliente = {}

        if 'direcciones' in data:
            direcciones = data['direcciones']
        else:
            direcciones = {}

        if 'ASES_CODIGO' in informacionCliente:
            ases_codigo = informacionCliente['ASES_CODIGO']
            asesor = {
                'ASES_CODIGO': ases_codigo
            }
        else:
            ases_codigo = None
            asesor = None

        if 'observaciones' in data:
            observaciones = data['observaciones']
        else:
            observaciones = {}

        if 'cuentas' in data:
            cuentas = data['cuentas']
        else:
            cuentas = {}

        if 'vinculos' in data:
            vinculos = data['vinculos']
        else:
            vinculos = {}

        # Inicio Reservar información a manejar del Cliente a partir del REQUEST
        secuencia = Secuencia.objects.using('clientes').filter(SECU_TABLA = 'CLIENTE', EMPR_CODIGO = '8').first()
        clie_codigo = secuencia.SECU_VALOR_ACTUAL
        ticl_codigo = informacionCliente['TICL_CODIGO']
        clie_identificacion = informacionCliente['CLIE_IDENTIFICACION']
        # Fin Reservar

        # Inicio Validar-Cliente
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = clie_identificacion).first()
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")

        if clienteChecking:
            clie_codigo = clienteChecking.CLIE_CODIGO
            actualizarC = actualizarCliente(informacionCliente, clienteChecking)
            if ticl_codigo == 'N':
                detalleCliente = ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
                actualizarDC = actualizarClienteNatural(detallesCliente, detalleCliente)
                log[logIndex] = f"El Cliente: {clie_identificacion} de tipo: {clienteChecking.TICL_CODIGO} ya está registrado, actualizando {actualizarC} campos de Cliente y {actualizarDC} campos de Cliente N. Pasando a Direcciones, Teléfonos, Observaciones y Asesores"
            if ticl_codigo == 'J':
                detalleCliente = ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
                actualizarDC = actualizarClienteJuridico(detallesCliente, detalleCliente)
                log[logIndex] = f"El Cliente: {clie_identificacion} de tipo: {clienteChecking.TICL_CODIGO} ya está registrado, actualizando {actualizarC} campos de Cliente y {actualizarDC} campos de Cliente J. Pasando a Direcciones, Teléfonos, Observaciones y Asesores"
            logIndex += 1
        else:
            informacionCliente['CLIE_FECHA_CREACION'] = d1
            informacionCliente['CLIE_TIPO_PROYECTO'] = 2
            informacionCliente['CLIE_CODIGO'] = clie_codigo
            informacionCliente['TISB_CODIGO'] = 1
            detallesCliente['CLIE_CODIGO'] = clie_codigo
            # Guardar CLIENTE
            validarC = validarCliente(informacionCliente)
            if validarC['status'] is False:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "log": validarC['log']})
            else:
                log[logIndex] = validarC['log']
                logIndex += 1

            if ticl_codigo == 'N':
                    # Guardar CLIENTE NATURAL
                    validarCN = validarClienteNatural(detallesCliente)
                    if validarCN['status'] is False:
                        return Response({"status": status.HTTP_400_BAD_REQUEST, "log": validarCN['log']})
                    else:
                        log[logIndex] = validarCN['log']
                        logIndex += 1
                    
                    guardarC = guardarCliente(informacionCliente)
                    log[logIndex] = guardarC['message']
                    logIndex += 1

                    guardarCN = guardarClienteNatural(detallesCliente)
                    log[logIndex] = guardarCN['message']
                    logIndex += 1
            elif ticl_codigo == 'J':
                # Guardar CLIENTE JURIDICO
                validarCJ = validarClienteJuridico(detallesCliente)
                if validarCJ['status'] is False:
                    return Response({"status": status.HTTP_400_BAD_REQUEST, "log": validarCJ['log']})
                else:
                    log[logIndex] = validarCJ['log']
                    logIndex += 1

                guardar = guardarCliente(informacionCliente)
                log[logIndex] = guardar['message']
                logIndex += 1
                
                guardarJ = guardarClienteJuridico(detallesCliente)
                log[logIndex] = guardarJ['message']
                logIndex += 1
            else:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "log": "Tipo de Cliente no válido"})

            secuencia = Secuencia.objects.using('clientes').filter(SECU_TABLA = 'CLIENTE', EMPR_CODIGO = '8').update(SECU_VALOR_ACTUAL = clie_codigo + 1)
            log[logIndex] = f'Se actualizó Secuencia actual de -> {clie_codigo} a -> {clie_codigo + 1}'
            logIndex += 1
        # Guardar Dirección
        for direccion in direcciones:
            if 'telefonos' in direccion:
                telefonos = direccion['telefonos']
            else:
                telefonos = {}
            dire_descripcion = direccion["DIRE_DESCRIPCION"]
            # Validar que la dirección enviada no esté registrado para el Cliente
            direccionExistente = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, DIRE_DESCRIPCION = dire_descripcion).first()
            if direccionExistente is None:
                direccion['DIRE_CODIGO'] = 1
                dire_codigo = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-DIRE_CODIGO').first()
                if dire_codigo:
                    direccion['DIRE_CODIGO'] = dire_codigo.DIRE_CODIGO + 1
                direccion['CLIE_CODIGO'] = clie_codigo
                direccion['CIUD_CODIGO'] = 223
                del(direccion['telefonos'])
                # Validar Ciudad
                validarD = validarDireccion(direccion)
                if validarD['status'] is False:
                    log[logIndex] = validarD['log']
                    logIndex += 1
                    continue
                else:
                    log[logIndex] = validarD['log']
                    logIndex += 1

                guardarD = guardarDireccion(direccion)
                log[logIndex] = guardarD['message']
                logIndex += 1
            else:
                direccion['DIRE_CODIGO'] = direccionExistente.DIRE_CODIGO
                log[logIndex] = f"La Dirección: {dire_descripcion} ya existe para el Cliente {clie_identificacion}"
                logIndex += 1

            # Validar que el número enviado no esté registrado para el Cliente
            for telefono in telefonos:
                tele_numero = telefono['TELE_NUMERO']
                telefonoExistente = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TELE_NUMERO = tele_numero).first()
                if telefonoExistente is None:
                    telefono['TELE_CODIGO'] = 1
                    tele_codigo = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-TELE_CODIGO').first()
                    if tele_codigo:
                        telefono['TELE_CODIGO'] = tele_codigo.TELE_CODIGO + 1
                    telefono['TIDE_CODIGO'] = direccion['TIDE_CODIGO']
                    telefono['DIRE_CODIGO'] = direccion['DIRE_CODIGO']
                    telefono['CLIE_CODIGO'] = clie_codigo

                    validarT = validarTelefono(telefono)
                    if validarT['status'] is False:
                        log[logIndex] = validarT['log']
                        logIndex += 1
                        continue
                    else:
                        log[logIndex] = validarT['log']
                        logIndex += 1

                    guardarT = guardarTelefono(telefono)
                    log[logIndex] = guardarT['message']
                    logIndex += 1
                else:
                    log[logIndex] = f"El Teléfono: {tele_numero} ya existe para el Cliente {clie_identificacion}."
                    logIndex += 1
        
        # Validar que el Cliente no tenga Asesor, en caso de que si, eliminarlo
        asesorClienteExiste = ClienteAsesor.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        if asesorClienteExiste != None:
            asesorClienteDuplicado = ClienteAsesor.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, ASES_CODIGO = ases_codigo).first()
            if asesorClienteDuplicado:
                log[logIndex] = f"El Cliente: {clie_identificacion} ya tiene asignado al Asesor: {asesorClienteExiste.ASES_CODIGO}"
                logIndex += 1
            else:
                log[logIndex] = f"El Cliente: {clie_identificacion} tenía asignado al Asesor: {asesorClienteExiste.ASES_CODIGO} y se actualizó al Asesor: {ases_codigo}"
                logIndex += 1
                ClienteAsesor.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).update(ASES_CODIGO = ases_codigo)
                Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = clie_identificacion).update(ASES_CODIGO = ases_codigo)
        else:
            # Guardar Asesor
            if asesor:
                asesor['CLIE_CODIGO'] = clie_codigo
                asesor['EMPR_CODIGO'] = 8
                guardarAC = guardarAsesorCliente(asesor)
                log[logIndex] = guardarAC['message']
                logIndex += 1
            else:
                log[logIndex] = f"Asesor no viene en la petición"
                logIndex += 1
        
        for observacion in observaciones:
            tioc_codigo = observacion['TIOC_CODIGO']
            observacion['CLIE_CODIGO'] = clie_codigo
            # Inicio Validar-Observaciones
            observacionExiste = Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TIOC_CODIGO = tioc_codigo).first()
            if observacionExiste:
                Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TIOC_CODIGO = tioc_codigo).update(OBCL_DESCRI = observacion['OBCL_DESCRI'])
                log[logIndex] = f"Se actualizó la descripción de la Observación: {observacionExiste.TIOC_CODIGO} a -> {observacion['OBCL_DESCRI']}"
                logIndex += 1
            else:
                observacion['OBCL_CODIGO'] = 1
                obcl_codigo = Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-OBCL_CODIGO').first()
                if obcl_codigo:
                    observacion['OBCL_CODIGO'] = obcl_codigo.OBCL_CODIGO + 1

                validarO = validarObservacion(observacion)
                if validarO['status'] is False:
                    log[logIndex] = validarO['log']
                    logIndex += 1
                    continue
                else:
                    log[logIndex] = validarO['log']
                    logIndex += 1
                
                guardarO = guardarObservacion(observacion)
                log[logIndex] = guardarO['message']
                logIndex += 1
        
        for cuenta in cuentas:
            ticu_codigo = cuenta['TICU_CODIGO']
            cubc_cuenta = cuenta['CUBC_CUENTA']
            cuenta['CLIE_CODIGO'] = clie_codigo
            cuentaExiste = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, CUBC_CUENTA = cubc_cuenta).first()
            if cuentaExiste is None:
                tipoCuentaExiste = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TICU_CODIGO = ticu_codigo).first()
                if tipoCuentaExiste:
                    banco = Banco.objects.using('clientes').filter(BANC_CODIGO = cuenta['BANC_CODIGO']).first()
                    if banco:
                        log[logIndex] = f"El Cliente: {clie_identificacion} tenía registrada la Cuenta Bancaria: {tipoCuentaExiste.CUBC_CUENTA} de tipo: {tipoCuentaExiste.TICU_CODIGO} y se actualizó a: {cubc_cuenta}"
                        logIndex += 1
                        CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TICU_CODIGO = ticu_codigo).update(CUBC_CUENTA = cubc_cuenta, BANC_CODIGO = cuenta['BANC_CODIGO'])
                    else:
                        log[logIndex] = f"La cuenta: {cubc_cuenta} no se puede actualizar porque el Banco: {cuenta['BANC_CODIGO']} no es válido"
                        logIndex += 1

                else:
                    cuenta['CUBC_CODIGO'] = 1
                    cubc_codigo = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-CUBC_CODIGO').first()
                    if cubc_codigo:
                        cuenta['CUBC_CODIGO'] = cubc_codigo.CUBC_CODIGO + 1

                    validarCB = validarCuenta(cuenta)
                    if validarCB['status'] is False:
                        log[logIndex] = validarCB['log']
                        logIndex += 1
                        continue
                    else:
                        log[logIndex] = validarCB['log']
                        logIndex += 1
                
                    guardarCB = guardarCuentaBancaria(cuenta)
                    log[logIndex] = guardarCB['message']
                    logIndex += 1
            else:
                log[logIndex] = f"La Cuenta Bancaria: {cubc_cuenta} ya existe para el Cliente: {clie_codigo}"
                logIndex += 1

        for vinculo in vinculos:
            vinc_identificacion = vinculo["VINC_IDENTIFICACION"]
            tivi_codigo = vinculo["TIVI_CODIGO"]
            vinculo['VIN_FECHA_INGRESA'] = d1
            # Validar que el vínculo enviado no esté registrado para el Cliente
            vinculoExistente = Vinculo.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, VINC_IDENTIFICACION = vinc_identificacion).first()
            if vinculoExistente is None:
                vinculo['VINC_CODIGO'] = 1
                vinc_codigo = Vinculo.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-VINC_CODIGO').first()
                if vinc_codigo:
                    vinculo['VINC_CODIGO'] = vinc_codigo.VINC_CODIGO + 1
                vinculo['CLIE_CODIGO'] = clie_codigo
                vinculo['TICL_CODIGO'] = ticl_codigo
                vinculo['VIN_ESTADO'] = "A"
                if ticl_codigo == 'N' and tivi_codigo == 1:
                    vinculo['esci_codigo'] = 1
                # Validar Ciudad
                validarV = validarVinculo(vinculo)
                if validarV['status'] is False:
                    log[logIndex] = validarV['log']
                    logIndex += 1
                    continue
                else:
                    log[logIndex] = validarV['log']
                    logIndex += 1

                guardarV = guardarVinculo(vinculo)
                log[logIndex] = guardarV['message']
                logIndex += 1

        #Fin Validar-Cliente
        return Response({"status": status.HTTP_200_OK, "log": log})
