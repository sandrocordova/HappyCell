from rest_framework import serializers
from apps.agencia.models import Post


# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = ['id','tittle','content']
        fields = '__all__'
        
