from rest_framework import serializers
from apps.catalog.models import TipoDocumento, TipoEmpresa, TipoClase, TipoProyecto, Profesion, Nacionalidad, ActividadEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral
from apps.catalog.models import TipoDireccion, CiudadCat, ZonaCat, PaisCat, TipoTelefono, Provincia, Canton, Parroquia, TipoVinculo, TipoObservacion

        #Catalogos

class TipoObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObservacion
        fields = '__all__'

class TipoVinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVinculo
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'
        
class CantonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canton
        fields = '__all__'

class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquia
        fields = '__all__'

class TipoTelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTelefono
        fields = '__all__'
        
class TipoDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDireccion
        fields = '__all__'
        
class PaisSerializerCat(serializers.ModelSerializer):
    class Meta:
        model = PaisCat
        fields = '__all__'
        
class ZonaSerializerCat(serializers.ModelSerializer):
    class Meta:
        model = ZonaCat
        fields = '__all__'

class CiudadSerializerCat(serializers.ModelSerializer):
    class Meta:
        model = CiudadCat
        fields = '__all__'
        
class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class TipoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpresa
        fields = '__all__'
        
class TipoClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoClase
        fields = '__all__'
        
class TipoProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProyecto
        fields = '__all__'
        
class ProfesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = '__all__'

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class ActiEconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadEconomica
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
        