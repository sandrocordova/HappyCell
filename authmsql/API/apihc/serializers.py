from dataclasses import fields
from rest_framework import serializers
from .models import Asesor, Ciudad, Cliente, ClienteJuridico, ClienteNatural, Direccion, GrupoEconomico, Nacionalidad, Pais, TipoCliente, TipoDireccion, TipoDocumento, TipoEmpresa, Usuario, Zona, ActividadEconómica, Profesion, NivelInstruccion, Sexo, EstadoCivil, Vivienda, SituacionLaboral

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'USUA_CODIGO', 
            'ESUS_CODIGO', 
            'USUA_NOMBRE', 
            'USUA_CLAVE', 
            'USUA_FECHA_CREACION', 
            'USUA_FECHA_INICIO',
            'USUA_FECHA_FIN',
            'USUA_LOGIN',
            'ZONA_CODIGO',
            'EMPR_CODIGO',
            'AGEN_CODIGO',
            'CETC_CODIGO',
            'USUA_IDENTIFICACION',
            'USUA_PERIOCIDAD',
            'USUA_ADMINISTRADOR',
            'USUA_CARGO'
            ]

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCliente
        fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class ActividadEconómicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadEconómica
        fields = '__all__'

class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesor
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    NACI_CODIGO = NacionalidadSerializer(read_only = True)
    TICL_CODIGO = TipoClienteSerializer(read_only = True)
    TIDO_CODIGO = TipoDocumentoSerializer(read_only = True)
    ACTI_CODIGO = ActividadEconómicaSerializer(read_only = True)
    ASES_CODIGO = AsesorSerializer(read_only = True)
    class Meta:
        model = Cliente
        fields = '__all__'

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class ZonaSerializer(serializers.ModelSerializer):
    PAIS_CODIGO = PaisSerializer(read_only = True)
    class Meta:
        model = Zona
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    ZONA_CODIGO = ZonaSerializer(read_only = True)
    class Meta:
        model = Ciudad
        fields = '__all__'

class TipoDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDireccion
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    CIUD_CODIGO = CiudadSerializer(read_only = True)
    TIDE_CODIGO = TipoDireccionSerializer(read_only = True)
    class Meta:
        model = Direccion
        fields = '__all__'

class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = '__all__'    

class NivelInstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelInstruccion
        fields = '__all__'     

class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = '__all__'     

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'        

class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = '__all__'
        
class SituacionLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionLaboral
        fields = '__all__'

class ClienteNaturalSerializer(serializers.ModelSerializer):
    PROF_CODIGO = ProfesionSerializer(read_only = True)
    NIIN_CODIGO = NivelInstruccionSerializer(read_only = True)
    SEXO_CODIGO = SexoSerializer(read_only = True)
    ESCI_CODIGO = EstadoCivilSerializer(read_only = True)
    CLIE_TIPO_VIVIENDA = ViviendaSerializer(read_only = True)
    CLIE_SITUACION_LABORAL = SituacionLaboralSerializer(read_only = True)
    class Meta:
        model = ClienteNatural
        fields = '__all__'

class GrupoEconomicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoEconomico
        fields = '__all__'
        
class TipoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmpresa
        fields = '__all__'

class ClienteJuridicoSerializer(serializers.ModelSerializer):
    TIEM_CODIGO = TipoEmpresaSerializer(read_only = True)
    GREC_CODIGO = GrupoEconomicoSerializer(read_only = True)
    class Meta:
        model = ClienteJuridico
        fields = '__all__'