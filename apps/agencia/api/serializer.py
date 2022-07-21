from rest_framework import serializers
from apps.agencia.models import Empresa


# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        #fields = ['id','tittle','content']
        fields = '__all__'
        
