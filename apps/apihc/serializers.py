from rest_framework import serializers
from apps.catalog.models import Agencia, Banco, Ciudad, CuentaBalance, GrupoEconomico, Moneda, Nacionalidad, Pais, Periocidad, SubtipoEmpresa, TipoAgencia, TipoAsesor, TipoBanca, TipoCliente, TipoCuenta, TipoCuentaBalance, TipoDireccion, TipoDocumento, TipoEmpresa, TipoObservacion, TipoTelefono, VehiculoLegal, Zona, ActividadEconomica, Profesion, NivelInstruccion, Sexo, EstadoCivil, Vivienda, SituacionLaboral
from .models import Asesor, BalanceCliente, Cliente, ClienteAsesor, ClienteJuridico, ClienteNatural, CuentaBancariaCliente, Direccion, Empresa, Observacion, Telefono, Usuario
from apps.catalog.serializer import TipoEmpresaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCliente
        fields = '__all__'


class ActividadEconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadEconomica
        fields = '__all__'

class TipoAsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAsesor
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
    class Meta:
        model = Ciudad
        fields = '__all__'

class VehiculoLegalSerializer(serializers.ModelSerializer):
    PAIS_CODIGO = PaisSerializer(read_only = True)
    class Meta:
        model = VehiculoLegal
        fields = '__all__'

class SubtipoEmpresaSerializer(serializers.ModelSerializer):
    TIEM_CODIGO = TipoEmpresaSerializer(read_only = True)
    class Meta:
        model = SubtipoEmpresa
        fields = '__all__'
    
class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'

class PeriocidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periocidad
        fields = '__all__'

class GrupoEconomicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoEconomico
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    VELE_CODIGO = VehiculoLegalSerializer(read_only = True)
    TIEM_CODIGO = TipoEmpresaSerializer(read_only = True)
    SUTE_CODIGO = SubtipoEmpresaSerializer(read_only = True)
    MONE_CODIGO = MonedaSerializer(read_only = True)
    GREM_CODIGO = GrupoEconomicoSerializer(read_only = True)
    PERI_CODIGO = PeriocidadSerializer(read_only = True)
    class Meta:
        model = Empresa
        fields = '__all__'



class TipoBancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBanca
        fields = '__all__'

class TipoAgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAgencia
        fields = '__all__'

class AgenciaSerializer(serializers.ModelSerializer):
    ZONA_CODIGO = ZonaSerializer(read_only = True)
    EMPR_CODIGO = EmpresaSerializer(read_only = True)
    TIAG_CODIGO = TipoAgenciaSerializer(read_only = True)
    CIUD_CODIGO = CiudadSerializer(read_only = True)
    class Meta:
        model = Agencia
        fields = '__all__'

class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesor
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    # NACI_CODIGO = NacionalidadSerializer(read_only = True)
    # TICL_CODIGO = TipoClienteSerializer(read_only = True)
    # TIDO_CODIGO = TipoDocumentoSerializer(read_only = True)
    # ACTI_CODIGO = ActividadEconomicaSerializer(read_only = True)
    # ASES_CODIGO = AsesorSerializer(read_only = True)
    class Meta:
        model = Cliente
        fields = '__all__'

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'

class TipoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuenta
        fields = '__all__'

class CuentaBancariaClienteSerializer(serializers.ModelSerializer):
    CLIE_CODIGO = ClienteSerializer(read_only = True)
    BANC_CODIGO = BancoSerializer(read_only = True)
    TICU_CODIGO = TipoCuentaSerializer(read_only = True)
    class Meta:
        model = CuentaBancariaCliente
        fields = '__all__'

class TipoCuentaBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuentaBalance
        fields = '__all__'

class CuentaBalanceSerializer(serializers.ModelSerializer):
    TICB_CODIGO = TipoCuentaBalanceSerializer(read_only = True)
    class Meta:
        model = CuentaBalance
        fields = '__all__'
    
class BalanceClienteSerializer(serializers.ModelSerializer):
    CUBA_CUENTA = CuentaBalanceSerializer(read_only = True)
    CLIE_CODIGO = ClienteSerializer(read_only = True)
    class Meta:
        model = BalanceCliente
        fields = '__all__'

class TipoObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObservacion
        fields = '__all__'

class ObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observacion
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = ClienteNatural
        fields = '__all__'

class ClienteJuridicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteJuridico
        fields = '__all__'


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'

class ClienteAsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteAsesor
        fields = '__all__'  