from rest_framework import serializers
from apps.agencia.models import Empresa, Usernav, Usernavtres, Cliente


# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['empr_codigo','empr_nombre','empr_identificacion']
        #fields = '__all__'
        
# Create your views here.
class UserNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usernav
        fields = '__all__'
        
        
        # Create your views here.
class UserNavSerializerDos(serializers.ModelSerializer):
    class Meta:
        model = Usernavtres
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        