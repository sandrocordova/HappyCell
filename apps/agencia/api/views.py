from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.agencia.models import Empresa, Usernav, Usernavdos, Usernavtres
from apps.agencia.api.serializer import PostSerializer, UserNavSerializer, UserNavSerializerDos


@api_view(['GET'])
def usernav_api_view(request):
    
    if request.method == 'GET':
        consulta = Usernav.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='ADMINISTRADOR' and ms.MOSI_CODIGO= 1")
        serializer_empresas = UserNavSerializer(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
@api_view(['GET'])
def nav_infor_api_view(request):
    
    if request.method == 'GET':
        consulta = Usernavtres.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO=tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO=om.MOSI_CODIGO inner join perfil_ventana pf on um.MOSI_CODIGO=pf.MOSI_CODIGO inner join ventana ve ON PF.VENT_CODIGO=VE.VENT_CODIGO WHERE ve.VENT_DESCRIPCION like 'WEB%' AND u.USUA_CODIGO='ADMINISTRADOR' and um.MOSI_CODIGO in (4,8,10) and om.OPME_DESCRIPCION like 'WEB%' AND PF.VENT_CODIGO like '8%'")  
        serializer_empresas = UserNavSerializerDos(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)

#Detalles de un elemento
@api_view(['GET'])
def detail_view_set(request, pk=None):
    
    if request.method == 'GET':
        #Script que retorne un elemento
        consulta = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        #Buscar entre una lista al elemento
        consulta = Empresa.objects.filter(id = pk).first()  
        serializer_empresas = PostSerializer(consulta)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
  
#Listar y guardar  
@api_view(['GET','POST'])
def PostApiViewSet_Post(request):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer_empresas = PostSerializer(data = request.data)
        if serializer_empresas.isValid():
            serializer_empresas.save()
            return Response(serializer_empresas.data, status = status.HTTP_200_OK)
        return Response(serializer_empresas.errors, status = status.HTTP_400_BAD_REQUEST)

#Actualizar  
@api_view(['GET','PUT'])
def PostApiViewSet_Post(request, pk=None):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        #Buscar entre una lista al elemento o recibir el elemento a actualizar
        consulta = Empresa.objects.filter(id = pk).first()  
        #Pasamos el objeto al serializador y lo actualiza con la data enviada
        #return response({message:'Mensaje Cualquiera'})
        serializer_empresas = PostSerializer(consulta, data = request.data)
        if serializer_empresas.is_valid():
            serializer_empresas.save()
            return response(serializer_empresas.data, status = status.HTTP_200_OK)
        return response(serializer_empresas.errors, status = status.HTTP_400_BAD_REQUEST)

    

