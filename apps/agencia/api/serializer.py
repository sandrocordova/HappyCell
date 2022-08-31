from rest_framework import serializers
from apps.agencia.models import Empresa, UsuarioInfo, UsuarioMenu

# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empr_codigo','empr_nombre','empr_identificacion']
        
class UsuarioInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioInfo
        fields = '__all__'
        
class UsuarioMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioMenu
        fields = '__all__'