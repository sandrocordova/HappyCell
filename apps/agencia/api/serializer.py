from rest_framework import serializers
from apps.agencia.models import Empresa


# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empr_codigo','empr_nombre','empr_identificacion']
        #fields = '__all__'
        
