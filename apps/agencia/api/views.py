from rest_framework import APIView
from rest_framework.response import Response
from apps.agencia.models import Empresa
from apps.agencia.api.serializer import PostSerializer


# Create your views here.
class PostApiViewSet(APIView):
    
    def get(self, request):
        empresas = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        #serializer_empresas = PostSerializer(empresas)
        serializer_empresas = PostSerializer(empresas, many = True)
        return Response(serializer_empresas.data)
    
    
