from rest_framework import serializers
from apps.agencia.models import Empresa, Usernav


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
        
        