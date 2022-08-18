from rest_framework import serializers
from apps.catalog.models import Profesiones, Nacionalidad, ActiEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral

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
        