from django.db import models

# Create your models here.
cascade_delete = models.CASCADE

class Usuario(models.Model):
    USUA_CODIGO = models.CharField(max_length = 20, primary_key = True)
    ESUS_CODIGO = models.PositiveIntegerField()
    USUA_NOMBRE = models.CharField(max_length = 40)
    USUA_CLAVE = models.CharField(max_length = 20)
    USUA_FECHA_CREACION = models.DateTimeField()
    USUA_FECHA_INICIO = models.DateTimeField()
    USUA_FECHA_FIN = models.DateTimeField()
    USUA_LOGIN = models.CharField(max_length = 20)
    ZONA_CODIGO = models.PositiveIntegerField()
    EMPR_CODIGO = models.CharField(max_length = 10)
    AGEN_CODIGO = models.PositiveIntegerField()
    CETC_CODIGO = models.PositiveIntegerField()
    USUA_IDENTIFICACION = models.CharField(max_length = 15)
    USUA_PERIOCIDAD = models.PositiveIntegerField()
    USUA_ADMINISTRADOR = models.CharField(max_length = 1)
    USUA_CARGO = models.CharField(max_length = 40)

    class Meta:
        db_table = "USUARIO"

class Nacionalidad(models.Model):
    NACI_CODIGO = models.PositiveIntegerField(primary_key = True)
    NACI_DESCRIPCION = models.CharField(max_length=40)

    class Meta:
        db_table = "NACIONALIDAD"

class TipoCliente(models.Model):
    TICL_CODIGO = models.CharField(max_length = 2, primary_key = True)
    TICL_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "TIPO_CLIENTE"

class TipoDocumento(models.Model):
    TICL_CODIGO = models.PositiveIntegerField()
    TIDO_CODIGO = models.CharField(max_length = 2, primary_key = True)
    TIDO_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "TIPO_DOCUMENTO"
        unique_together = (("TICL_CODIGO", "TIDO_CODIGO"))

class ActividadEconomica(models.Model):
    ACTI_CODIGO = models.PositiveIntegerField(primary_key = True)
    ACTI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "ACTIVIDAD_ECONOMICA"

class TipoAsesor(models.Model):
    TIAS_CODIGO = models.AutoField(primary_key = True)
    TIAS_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_ASESOR'

class Pais(models.Model):
    PAIS_CODIGO = models.CharField(max_length = 3, primary_key = True)
    PAIS_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'PAIS'

class VehiculoLegal(models.Model):
    VELE_CODIGO = models.CharField(primary_key = True, max_length = 3)
    PAIS_CODIGO = models.ForeignKey(Pais, on_delete = cascade_delete, db_column = 'PAIS_CODIGO')
    VELE_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'VEHICULO_LEGAL'

class TipoEmpresa(models.Model):
    TIEM_CODIGO = models.AutoField(primary_key = True)
    TIEM_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_EMPRESA'

class SubtipoEmpresa(models.Model):
    TIEM_CODIGO = models.ForeignKey(TipoEmpresa, on_delete = cascade_delete, db_column = 'TIEM_CODIGO')
    SUTE_CODIGO = models.AutoField(primary_key = True)
    SUTE_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'SUB_TIPO_EMPRESA'

class Moneda(models.Model):
    MONE_CODIGO = models.CharField(primary_key = True, max_length = 3)
    MONE_DESCRIPCION = models.CharField(max_length = 40)
    MONE_DECIMALES = models.PositiveIntegerField()
    MONE_ALIAS = models.CharField(max_length = 3)

    class Meta:
        db_table = 'MONEDA'

class Periocidad(models.Model):
    PERI_CODIGO = models.AutoField(primary_key = True)
    PERI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'PERIOCIDAD'

class GrupoEconomico(models.Model):
    GREC_CODIGO = models.AutoField(primary_key = True)
    GREC_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "GRUPO_ECONOMICO"

class Empresa(models.Model):
    EMPR_CODIGO = models.CharField(primary_key = True, max_length = 10)
    EMP_EMPR_CODIGO = models.CharField(null = True, max_length = 10)
    VELE_CODIGO = models.ForeignKey(VehiculoLegal, on_delete = cascade_delete, db_column = 'VELE_CODIGO')
    TIEM_CODIGO = models.ForeignKey(TipoEmpresa, on_delete = cascade_delete, db_column = 'TIEM_CODIGO')
    SUTE_CODIGO = models.ForeignKey(SubtipoEmpresa, on_delete = cascade_delete, db_column = 'SUTE_CODIGO')
    MONE_CODIGO = models.ForeignKey(Moneda, on_delete = cascade_delete, db_column = 'MONE_CODIGO')
    EMPR_NOMBRE = models.CharField(max_length = 80)
    EMPR_IDENTIFICACION = models.CharField(max_length = 20)
    EMPR_FECHA_CONSTITUCION = models.DateTimeField()
    EMPR_FECHA_CREACION = models.DateTimeField()
    EMPR_DIRECCION = models.CharField(max_length = 80)
    FECHA_ACTUAL = models.DateTimeField()
    FECHA_ANTERIOR = models.DateTimeField()
    FECHA_SIGUIENTE = models.DateTimeField()
    GREM_CODIGO = models.ForeignKey(GrupoEconomico, on_delete = cascade_delete, db_column = 'GREM_CODIGO')
    PERI_CODIGO = models.ForeignKey(Periocidad, on_delete = cascade_delete, db_column = 'PERI_CODIGO')
    FECHA_CIERRE = models.DateTimeField(null = True)
    EMPR_VIGENTE = models.CharField(max_length = 1)
    EMPR_PERIOCIDAD = models.PositiveIntegerField()
    EMPR_CODIGO_SUPER = models.CharField(null = True, max_length = 20)
    empr_rep_legal = models.CharField(null = True, max_length = 50)
    empr_cargo = models.CharField(null = True, max_length = 30)
    autorizacion_sri = models.CharField(null = True, max_length = 30)
    contribuyente_esp = models.CharField(null = True, max_length = 50)
    empr_fecha_emision = models.CharField(null = True, max_length = 30)
    EMPR_IMPRIME_IMAGEN = models.PositiveIntegerField(null = True)
    EMPR_IMAGEN = models.CharField(null = True, max_length = 50)

    class Meta:
        db_table = 'EMPRESA'

class Zona(models.Model):
    ZONA_CODIGO = models.AutoField(primary_key = True)
    PAIS_CODIGO = models.ForeignKey(Pais, on_delete = cascade_delete, db_column = 'PAIS_CODIGO')
    ZONA_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'ZONA'

class Ciudad(models.Model):
    ZONA_CODIGO = models.ForeignKey(Zona, on_delete = cascade_delete, db_column = 'ZONA_CODIGO')
    CIUD_CODIGO = models.AutoField(primary_key = True)
    CIUD_NOMBRE = models.CharField(max_length = 50)

    class Meta:
        db_table = 'CIUDAD'

class TipoBanca(models.Model):
    TIBA_CODIGO = models.AutoField(primary_key = True)
    TIBA_DESCRIPCION = models.CharField(max_length = 40)
    TIBA_RESPONSABLE = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_DE_BANCA'

class TipoAgencia(models.Model):
    TIAG_CODIGO = models.AutoField(primary_key = True)
    TIAG_DESCRIPCION = models.CharField(max_length = 40)
    TIAG_CENTRO_CANJE = models.CharField(max_length = 2
    )
    class Meta:
        db_table = 'TIPO_AGENCIA'

class Agencia(models.Model):
    ZONA_CODIGO = models.ForeignKey(Zona, on_delete = cascade_delete, db_column = 'ZONA_CODIGO')
    EMPR_CODIGO = models.ForeignKey(Empresa, on_delete = cascade_delete, db_column = 'EMPR_CODIGO')
    AGEN_CODIGO = models.AutoField(primary_key = True)
    TIAG_CODIGO = models.ForeignKey(TipoAgencia, on_delete = cascade_delete, db_column = 'TIAG_CODIGO')
    AGEN_DESCRIPCION = models.CharField(max_length = 40)
    AGEN_DIRECCION = models.CharField(max_length = 40)
    AGEN_RESPONSABLE = models.CharField(max_length = 40)
    AGEN_TELEFONO = models.CharField(max_length = 40)
    AGEN_CODIGO_SUPER = models.CharField(max_length = 40, null = True)
    CIUD_CODIGO = models.ForeignKey(Ciudad, on_delete = cascade_delete, db_column= 'CIUD_CODIGO')

    class Meta:
        db_table = 'AGENCIA'

class Asesor(models.Model):
    ASES_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIAS_CODIGO = models.PositiveIntegerField()
    ASE_ASES_CODIGO = models.PositiveIntegerField(null = True)
    TIBA_CODIGO = models.PositiveIntegerField()
    ZONA_CODIGO = models.PositiveIntegerField()
    EMPR_CODIGO = models.CharField(max_length = 10)
    AGEN_CODIGO = models.PositiveIntegerField()
    USUA_CODIGO = models.CharField(max_length = 20)
    ASES_NOMBRE = models.CharField(max_length = 40)
    ASES_CLAVE = models.CharField(max_length = 40)

    class Meta:
        db_table = "ASESOR"

class Cliente(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField(primary_key = True)	
    NACI_CODIGO	= models.PositiveIntegerField()
    TICL_CODIGO	= models.CharField(max_length = 2)
    TIDO_CODIGO	= models.CharField(max_length = 2)
    ACTI_CODIGO	= models.PositiveIntegerField()
    ASES_CODIGO	= models.PositiveIntegerField()
    CLIE_IDENTIFICACION	= models.CharField(max_length =	20)
    CLIE_NOMBRE	= models.CharField(max_length =	60, null = True)
    CLIE_FECHA_CREACION	= models.DateTimeField(null = True)	
    CLIE_NOMBRE_CORRESPONDENCIA	= models.CharField(max_length =	40)
    clie_estado	= models.CharField(max_length =	1, null = True)
    TISB_CODIGO	= models.PositiveIntegerField(null = True)	
    clie_tipo = models.CharField(max_length = 1, null = True)
    CLIE_CLAVE = models.CharField(max_length = 20, null = True)
    CLIE_TIPO_ROL = models.CharField(max_length = 2, null = True)
    CLIE_TIPO_PROYECTO = models.PositiveIntegerField(null = True)	
    comodin	= models.PositiveIntegerField(null = True)	
    ASES = models.PositiveIntegerField(null = True)	
    CLIE_FECHA_INACTIVACION	= models.DateTimeField(null = True)	
    CLIE_FECHA_DESAFILIACION = models.DateTimeField(null = True)	
    sect_codigo	= models.CharField(max_length =	5, null = True)
    pais_codigo	= models.CharField(max_length =	3, null = True)
    prov_codigo	= models.CharField(max_length =	3, null = True)
    cant_codigo	= models.CharField(max_length =	5, null = True)
    parr_codigo	= models.CharField(max_length =	5, null = True)

    class Meta:
        db_table = "CLIENTE"

class Banco(models.Model):
    BANC_CODIGO = models.PositiveIntegerField(primary_key = True)
    BANC_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'BANCO'

class TipoCuenta(models.Model):
    TICU_CODIGO = models.PositiveIntegerField(primary_key = True)
    TICU_DESCRIPCION = models.CharField(max_length = 40)
    TICU_CODIGO_ALT = models.CharField(max_length = 5)

    class Meta:
        db_table = 'TIPO_CUENTA'

class CuentaBancariaCliente(models.Model):
    CLIE_CODIGO = models.PositiveIntegerField()
    CUBC_CODIGO = models.PositiveIntegerField(primary_key = True)
    BANC_CODIGO = models.PositiveIntegerField()
    TICU_CODIGO = models.PositiveIntegerField()
    CUBC_CUENTA = models.CharField(max_length = 20)
    CUBC_CUENTA_CONTABLE = models.CharField(max_length = 40, null = True)
    PROPIETARIO_CUENTA = models.CharField(max_length = 250, null = True)

    class Meta:
        db_table = 'CUENTA_BANCARIA_CLIENTE'

class TipoCuentaBalance(models.Model):
    TICB_CODIGO = models.PositiveIntegerField(primary_key = True)
    TICB_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_CUENTA_BALANCE'

class CuentaBalance(models.Model):
    CUBA_CUENTA = models.AutoField(primary_key = True)
    TICB_CODIGO = models.ForeignKey(TipoCuentaBalance, on_delete = cascade_delete, db_column = 'TICB_CODIGO')
    CUBA_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'CUENTA_BALANCE'

class BalanceCliente(models.Model):
    CUBA_CUENTA = models.ForeignKey(CuentaBalance, on_delete = cascade_delete, db_column = 'CUBA_CUENTA')
    CLIE_CODIGO = models.ForeignKey(Cliente, on_delete = cascade_delete, db_column = 'CLIE_CODIGO')
    BAEM_FECHA = models.DateTimeField(primary_key = True)
    BAEM_VALOR = models.DecimalField(max_digits = 5, decimal_places = 4)

    class Meta:
        db_table = 'BALANCE_CLIENTE'
        unique_together = ((
            "CUBA_CUENTA", 
            "CLIE_CODIGO", 
            "BAEM_FECHA"
            ))

class TipoObservacion(models.Model):
    TIOC_CODIGO = models.AutoField(primary_key = True)
    TIOC_DESCRI = models.CharField(max_length = 40)
    TIOC_CAMBIO = models.PositiveIntegerField()

    class Meta:
        db_table = 'TIPO_OBSERVACION_CLIENTE'

class Observacion(models.Model):
    CLIE_CODIGO = models.PositiveIntegerField()
    OBCL_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIOC_CODIGO = models.PositiveIntegerField()
    OBCL_DESCRI = models.CharField(max_length = 4000)

    class Meta:
        db_table = 'OBSERVACION_CLIENTES'

class TipoDireccion(models.Model):
    TIDE_CODIGO = models.AutoField(primary_key = True)
    TIDE_DESCRIPCION = models.CharField(max_length = 40)
    class Meta:
        db_table = 'TIPO_DIRECCION'

class Direccion(models.Model):
    TIDE_CODIGO = models.PositiveIntegerField()
    CLIE_CODIGO = models.PositiveIntegerField()
    DIRE_CODIGO = models.PositiveIntegerField(primary_key = True)
    CIUD_CODIGO = models.PositiveIntegerField()
    DIRE_DESCRIPCION = models.CharField(max_length = 250, null = True)
    prov_codigo	= models.CharField(max_length =	5, null = True)
    cant_codigo	= models.CharField(max_length =	5, null = True)
    parr_codigo	= models.CharField(max_length =	5, null = True)
    
    class Meta:
        db_table = 'DIRECCION'
        unique_together = (("CLIE_CODIGO", "DIRE_CODIGO"))

class Profesion(models.Model):
    PROF_CODIGO = models.AutoField(primary_key = True)
    PROF_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "PROFESION"

class NivelInstruccion(models.Model):
    NIIN_CODIGO = models.AutoField(primary_key = True)
    NIIN_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "NIVEL_INSTRUCCION"

class Sexo(models.Model):
    SEXO_CODIGO = models.CharField(primary_key = True, max_length = 3)
    SEXO_DESCRIPCION = models.CharField(max_length = 40)
    
    class Meta:
        db_table = "SEXO"

class EstadoCivil(models.Model):
    ESCI_CODIGO = models.AutoField(primary_key = True)
    ESCI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "ESTADO_CIVIL"

class Vivienda(models.Model):
    VIVI_CODIGO = models.AutoField(primary_key = True)
    VIVI_DESCRIPCION = models.CharField(max_length = 50)

    class Meta:
        db_table = "VIVIENDA"
    
class SituacionLaboral(models.Model):
    SITL_CODIGO = models.AutoField(primary_key = True)
    SITL_DESCRIPCION = models.CharField(max_length = 50)

    class Meta:
        db_table = "SITUACION_LABORAL"

class ClienteNatural(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField(primary_key = True)
    PROF_CODIGO	= models.PositiveIntegerField()
    NIIN_CODIGO	= models.PositiveIntegerField()
    SEXO_CODIGO	= models.CharField(max_length = 2)
    ESCI_CODIGO	= models.PositiveIntegerField()
    CLNA_NOMBRE1 = models.CharField(max_length = 40)
    CLNA_NOMBRE2 = models.CharField(max_length = 40, null = True)
    CLNA_APELLIDO1 = models.CharField(max_length = 40)
    CLNA_APELLIDO2 = models.CharField(max_length = 40, null = True)
    CLNA_FECHA_NACIMIENTO = models.DateTimeField()
    CLNA_LUGAR_NACIMIENTO = models.CharField(max_length = 40)
    CLIE_TIPO_VIVIENDA = models.PositiveIntegerField(null = True)
    CLIE_SITUACION_LABORAL = models.PositiveIntegerField(null = True)
    CLNA_EXPIRA_PASAPORTE = models.DateTimeField(null = True)
    CLNA_INICIO_RESIDENCIA = models.DateTimeField(null = True)
    CLNA_NUM_CARGAS	= models.PositiveIntegerField(null = True)
    CLNA_EMPRESA_TRABAJA = models.CharField(max_length = 60, null = True)
    CLNA_INICIO_INGRESOS = models.DateTimeField(null = True)

    class Meta:
        db_table = "CLIENTE_NATURAL"

class ClienteJuridico(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField(primary_key = True)		
    # TIEM_CODIGO	= models.ForeignKey(TipoEmpresa, on_delete = cascade_delete, db_column = 'TIEM_CODIGO')	
    # GREC_CODIGO	= models.ForeignKey(GrupoEconomico, on_delete = cascade_delete, db_column = 'GREC_CODIGO')
    TIEM_CODIGO	= models.PositiveIntegerField()	
    GREC_CODIGO	= models.PositiveIntegerField()
    CLI_CLIE_CODIGO	= models.PositiveIntegerField()		
    CLJU_NOMBRE_PUBLICITARIO = models.CharField(max_length = 80)
    CLJU_RAZON_SOCIAL = models.CharField(max_length = 40)
    CLJU_REPRESENTANTE = models.CharField(max_length = 40)
    CLJU_FECHA_CONSTITUCION	= models.DateTimeField()
    CLJU_CAPITAL_SUS = models.DecimalField(max_digits = 15, decimal_places = 2)
    CLJU_CAPITAL_PAG = models.DecimalField(max_digits = 15, decimal_places = 2)
    CLJU_FECREF_STA	= models.DateTimeField()
    CLJU_RESERVA_LEG = models.DecimalField(max_digits = 15, decimal_places = 2)
    CLJU_CARGO_REPRESENTANTE = models.CharField(max_length = 40)

    class Meta:
        db_table = "CLIENTE_JURIDICO"

class TipoTelefono(models.Model):
    TITE_CODIGO = models.AutoField(primary_key = True)
    TITE_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_TELEFONO'

class Telefono(models.Model):
    TELE_CODIGO	= models.PositiveIntegerField(primary_key = True)
    TITE_CODIGO	= models.PositiveIntegerField()
    TIDE_CODIGO	= models.PositiveIntegerField()
    CLIE_CODIGO	= models.PositiveIntegerField()
    DIRE_CODIGO	= models.PositiveIntegerField()
    TELE_NUMERO	= models.CharField(max_length = 40)

    class Meta:
        db_table = 'TELEFONO'

class ClienteAsesor(models.Model):
    CLIE_CODIGO = models.PositiveIntegerField(primary_key = True)
    ASES_CODIGO = models.PositiveIntegerField()
    EMPR_CODIGO = models.CharField(max_length = 10)

    class Meta:
        db_table = 'CLIENTE_ASESOR'
        unique_together = ((
            "CLIE_CODIGO", 
            "ASES_CODIGO"
            ))

class Secuencia(models.Model):
    EMPR_CODIGO	= models.CharField(max_length =	10, null = True)
    SECU_TABLA = models.CharField(max_length =	40, primary_key = True)
    SECU_VALOR_ACTUAL = models.PositiveIntegerField()
    SECU_PASO = models.PositiveIntegerField()

    class Meta:
        db_table = 'SECUENCIAS'
        unique_together = ((
            "EMPR_CODIGO", 
            "SECU_TABLA"
            ))

class TipoProyecto(models.Model):
    COD_TIPO_PROYECTO = models.PositiveIntegerField(primary_key = True)
    DESC_TIPO_PROYECTO = models.CharField(max_length =	50, null = True)

    class Meta:
        db_table = 'CLIE_TIPO_PROYECTO'

class TipoRol(models.Model):
    TIRO_CODIGO = models.CharField(max_length = 2, primary_key = True)
    TIROL_DESCRIPCIÒN = models.CharField(max_length = 50)

    class Meta:
        db_table = 'TIPO_ROL'

class Provincia(models.Model):
    PAIS_CODIGO	= models.CharField(max_length =	3)
    PROV_CODIGO	= models.CharField(max_length =	5, primary_key = True)
    PROV_NOMBRE	= models.CharField(max_length =	50)

    class Meta:
        db_table = 'PROVINCIA'

class Canton(models.Model):
    PROV_CODIGO	= models.CharField(max_length =	5)
    CANT_CODIGO	= models.CharField(max_length =	5, primary_key = True)
    CANT_NOMBRE	= models.CharField(max_length =	50)

    class Meta:
        db_table = 'CANTON'

class Parroquia(models.Model):
    PROV_CODIGO	= models.CharField(max_length =	5)
    CANT_CODIGO	= models.CharField(max_length =	5)
    PARR_CODIGO	= models.CharField(max_length =	5, primary_key = True)
    PARR_NOMBRE	= models.CharField(max_length =	50)
    
    class Meta:
        db_table = 'PARROQUIA'

class Vinculo(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField()		
    VINC_CODIGO	= models.PositiveIntegerField(primary_key = True)		
    TICL_CODIGO	= models.CharField(max_length =	2)
    TIVI_CODIGO	= models.PositiveIntegerField()		
    VINC_IDENTIFICACION	= models.CharField(max_length =	20)
    VINC_NOMBRE	= models.CharField(max_length =	60, null = True)
    VINC_DIRECCION	= models.CharField(max_length =	80)
    VINC_TELEFONO = models.CharField(max_length =	40)
    VINC_OBSERVA = models.CharField(max_length =	400, null = True)
    VIN_USUARIO_INGRESA	= models.CharField(max_length =	50, null = True)
    VIN_FECHA_INGRESA = models.DateTimeField(null = True)
    VIN_ESTADO = models.CharField(max_length = 1, null = True)
    NACI_CODIGO	= models.PositiveIntegerField(null = True)
    PROF_CODIGO	= models.PositiveIntegerField(null = True)
    VINC_CARGO = models.CharField(max_length =	40, null = True)
    CIUD_CODIGO	= models.PositiveIntegerField(null = True)
    esci_codigo	= models.PositiveIntegerField(null = True)

    class Meta:
        db_table = 'VINCULO'
        unique_together = ((
            "CLIE_CODIGO", 
            "VINC_CODIGO"
            ))

class TipoVinculo(models.Model):
    TICL_CODIGO	= models.CharField(max_length =	2)
    TIVI_CODIGO	= models.PositiveIntegerField(primary_key = True)
    TIVI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_VINCULO'
        unique_together = ((
            "TICL_CODIGO", 
            "TIVI_CODIGO"
            ))
