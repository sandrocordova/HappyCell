from rest_framework.serializers import ModelSerializer
from agencia.models import Post


# Create your views here.
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','tittle','content']
    
