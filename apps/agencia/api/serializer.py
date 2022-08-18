from rest_framework import serializers
from apps.agencia.models import Empresa, Usernav, Usernavtres
from apps.agencia.models import Profesiones, Nacionalidad, ActiEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral
from apps.cliente.models import Cliente

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
        
        #Catalogos
class ProfesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesiones
        fields = '__all__'

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class ActiEconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiEconomica
        fields = '__all__'

class TipoRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRol
        fields = '__all__'

class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = '__all__'
class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = '__all__'
class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'
class SituacionLaboralCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionLaboral
        fields = '__all__'
        