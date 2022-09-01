from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.agencia.models import UsuarioInfo, UsuarioMenu
from apps.agencia.api.serializer import UsuarioInfoSerializer, UsuarioMenuSerializer
from apps.apihc.models import Usuario
from apps.usuario.views import authenticate
from apps.apihc.serializers import UsuarioSerializer
  
class cliente_search(APIView):
    def post(self, request):
        auth = authenticate(request)
        if auth['status'] is status.HTTP_200_OK:
            user = auth["Usuario"]["USUA_CODIGO"] 
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
                    json_response = {
                        'status': "200",
                        'message': "Response exitoso",
                        "data": 
                            [
                                {
                                    "user_profile":serializerUsuarioInfo.data,
                                    "menu_access": menuPadre,
                                }
                            ],
                    }
                    return Response(json_response, status = status.HTTP_200_OK)
                else: return Response({"status":"400","message":"El usuario no tiene acceso a menús"})
            else: return Response({"status":"400","message":"Rol de usuario no encontrado"})
        else: return Response({"status": status.HTTP_401_UNAUTHORIZED, "message": "Token inválido!"})

def obtener_hijos(opmeDescripcion, menuHijos):
    hijosReturn = []
    for hijo in menuHijos:
        if hijo["opme_descripcion"]==opmeDescripcion:
            hijosReturn.append(hijo)
    return hijosReturn

def login_validate(user, password):
    usuario = Usuario.objects.filter(USUA_LOGIN=user, USUA_CLAVE=password).first()
    if usuario:
        serializerUsuario = UsuarioSerializer(usuario)
        return True    
    return False

@api_view(['GET'])
def usernav_api_view(request):
    #OFICIAL
    if request.method == 'GET':
        consulta = Usernav.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='ADMINISTRADOR' and ms.MOSI_CODIGO= 1")
        if consulta:
            serializer_empresas = UserNavSerializer(consulta, many = True)
            return Response(serializer_empresas.data, status = status.HTTP_200_OK)
        return Response({"status":"400","message":"Usuario no encontrado"})
    
@api_view(['GET'])
def nav_infor_api_view(request):
    if request.method == 'GET':
        consulta = Usernavtres.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION, ve.vent_ventana FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO= tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO = om.MOSI_CODIGO inner join perfil_ventana pf on (om.opme_codigo = pf.OPME_CODIGO) inner join ventana ve ON (PF.VENT_CODIGO=VE.VENT_CODIGO and vent_ventana like '/%%') WHERE u.USUA_CODIGO = 'ADMINISTRADOR' and um.MOSI_CODIGO in (4,8,10) AND OM.OPME_CODIGO >= 800 order by om.opme_orden")  
        serializer_empresas = UserNavSerializerDos(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
