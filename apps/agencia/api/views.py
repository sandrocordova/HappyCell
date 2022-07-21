from django.db import connection
from rest_framework.viewsets import ModelViewSet
from apps.agencia.models import Post
from apps.agencia.api.serializer import PostSerializer


# Create your views here.
class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset= Post.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
    
