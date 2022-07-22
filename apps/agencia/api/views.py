from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.agencia.models import Empresa, Usernav
from apps.agencia.api.serializer import PostSerializer, UserNavSerializer


@api_view(['GET'])
def usernav_api_view(request):
    
    if request.method == 'GET':
        consulta = Usernav.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='ADMINISTRADOR' and ms.MOSI_CODIGO= 1")
        serializer_empresas = UserNavSerializer(consulta, many = True)
        return Response(serializer_empresas.data)
    
@api_view(['GET'])
def nav_infor_api_view(request):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data)
    
@api_view(['GET'])
def detail_view_set(request):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data)
    
@api_view(['GET','POST'])
def PostApiViewSet_Post(request):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data)
    
    elif request.method == 'POST':
        serializer_empresas = PostSerializer(data = request.data)
        if serializer_empresas.isValid():
            serializer_empresas.save()
            return Response(serializer_empresas.data)
        return Response(serializer_empresas.errors)

# Basado en clases.
class PostApiViewSetClass(APIView):
    
    def get(self, request):
        empresas = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        #serializer_empresas = PostSerializer(empresas)
        serializer_empresas = PostSerializer(empresas, many = True)
        return Response(serializer_empresas.data)
    
    

