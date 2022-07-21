from rest_framework import serializers
from apps.agencia.models import Empresa


# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['EMPR_CODIGO','EMPR_NOMBRE','EMPR_IDENTIFICACION']
        #fields = '__all__'
        
