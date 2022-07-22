from rest_framework.views import APIView
from rest_framework.response import Response
from apps.agencia.models import Empresa
from apps.agencia.api.serializer import PostSerializer

@api_view(['GET'])
def nav_api_view(request):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        serializer_empresas = PostSerializer(consulta, many = True)
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
    
    
