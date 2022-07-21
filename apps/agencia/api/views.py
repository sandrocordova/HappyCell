from django.db import connection
from rest_framework.viewsets import ModelViewSet
from agencia.models import Post
from agencia.api.serializer import PostSerializer


# Create your views here.
class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
