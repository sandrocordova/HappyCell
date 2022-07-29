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
    TICL_CODIGO = models.ForeignKey(TipoCliente, on_delete = models.DO_NOTHING, db_column = 'TICL_CODIGO')
    TIDO_CODIGO = models.CharField(max_length = 2, primary_key = True)
    TIDO_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "TIPO_DOCUMENTO"
        unique_together = (("TICL_CODIGO", "TIDO_CODIGO"))

class ActividadEconómica(models.Model):
    ACTI_CODIGO = models.PositiveIntegerField(primary_key = True)
    ACTI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "ACTIVIDAD_ECONOMICA"

class Asesor(models.Model):
    ASES_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIAS_CODIGO = models.PositiveIntegerField()
    ASE_ASES_CODIGO = models.PositiveIntegerField()
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
    CLIE_CODIGO	= models.AutoField(primary_key = True)	
    NACI_CODIGO	= models.ForeignKey(Nacionalidad, on_delete = cascade_delete, db_column = 'NACI_CODIGO')
    TICL_CODIGO	= models.ForeignKey(TipoCliente, on_delete = cascade_delete, db_column = 'TICL_CODIGO')
    TIDO_CODIGO	= models.ForeignKey(TipoDocumento, on_delete = cascade_delete, db_column = 'TIDO_CODIGO')
    ACTI_CODIGO	= models.ForeignKey(ActividadEconómica, on_delete = cascade_delete, db_column = 'ACTI_CODIGO')
    ASES_CODIGO	= models.ForeignKey(Asesor, on_delete = cascade_delete, db_column = 'ASES_CODIGO', null = True)
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

class Pais(models.Model):
    PAIS_CODIGO = models.CharField(max_length = 3, primary_key = True)
    PAIS_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'PAIS'
    
class Zona(models.Model):
    ZONA_CODIGO = models.PositiveIntegerField(primary_key = True)
    PAIS_CODIGO = models.ForeignKey(Pais, on_delete = cascade_delete, db_column = 'PAIS_CODIGO')
    ZONA_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'ZONA'

class Ciudad(models.Model):
    ZONA_CODIGO = models.ForeignKey(Zona, on_delete = cascade_delete, db_column = 'ZONA_CODIGO')
    CIUD_CODIGO = models.PositiveIntegerField(primary_key = True)
    CIUD_NOMBRE = models.CharField(max_length = 50)

    class Meta:
        db_table = 'CIUDAD'

class TipoDireccion(models.Model):
    TIDE_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIDE_DESCRIPCION = models.CharField(max_length = 40)
    class Meta:
        db_table = 'TIPO_DIRECCION'

class Direccion(models.Model):
    TIDE_CODIGO = models.ForeignKey(TipoDireccion, on_delete = cascade_delete, db_column = 'TIDE_CODIGO')
    CLIE_CODIGO = models.PositiveIntegerField()
    DIRE_CODIGO = models.PositiveIntegerField(primary_key = True)
    CIUD_CODIGO = models.ForeignKey(Ciudad, on_delete = cascade_delete, db_column = 'CIUD_CODIGO')
    DIRE_DESCRIPCION = models.CharField(max_length = 250)
    
    class Meta:
        db_table = 'DIRECCION'
        unique_together = (("CLIE_CODIGO", "DIRE_CODIGO"))

class Profesion(models.Model):
    PROF_CODIGO = models.PositiveIntegerField(primary_key = True)
    PROF_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "PROFESION"

class NivelInstruccion(models.Model):
    NIIN_CODIGO = models.PositiveIntegerField(primary_key = True)
    NIIN_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "NIVEL_INSTRUCCION"

class Sexo(models.Model):
    SEXO_CODIGO = models.CharField(primary_key = True, max_length = 3)
    SEXO_DESCRIPCION = models.CharField(max_length = 40)
    
    class Meta:
        db_table = "SEXO"

class EstadoCivil(models.Model):
    ESCI_CODIGO = models.PositiveIntegerField(primary_key = True)
    ESCI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "ESTADO_CIVIL"

class Vivienda(models.Model):
    VIVI_CODIGO = models.PositiveIntegerField(primary_key = True)
    VIVI_DESCRIPCION = models.CharField(max_length = 50)

    class Meta:
        db_table = "VIVIENDA"
    
class SituacionLaboral(models.Model):
    SITL_CODIGO = models.PositiveIntegerField(primary_key = True)
    SITL_DESCRIPCION = models.CharField(max_length = 50)

    class Meta:
        db_table = "SITUACION_LABORAL"

class ClienteNatural(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField(primary_key = True)
    PROF_CODIGO	= models.ForeignKey(Profesion, on_delete = cascade_delete, db_column = 'PROF_CODIGO')
    NIIN_CODIGO	= models.ForeignKey(NivelInstruccion, on_delete = cascade_delete, db_column = 'NIIN_CODIGO')
    SEXO_CODIGO	= models.ForeignKey(Sexo, on_delete = cascade_delete, db_column = 'SEXO_CODIGO')
    ESCI_CODIGO	= models.ForeignKey(EstadoCivil, on_delete = cascade_delete, db_column = 'ESCI_CODIGO')
    CLNA_NOMBRE1 = models.CharField(max_length = 40)
    CLNA_NOMBRE2 = models.CharField(max_length = 40)
    CLNA_APELLIDO1 = models.CharField(max_length = 40)
    CLNA_APELLIDO2 = models.CharField(max_length = 40)
    CLNA_FECHA_NACIMIENTO = models.DateTimeField()
    CLNA_LUGAR_NACIMIENTO = models.CharField(max_length = 40)
    CLIE_TIPO_VIVIENDA = models.ForeignKey(Vivienda, on_delete = cascade_delete, to_field = 'VIVI_CODIGO', db_column = 'CLIE_TIPO_VIVIENDA')
    CLIE_SITUACION_LABORAL = models.ForeignKey(SituacionLaboral, on_delete = cascade_delete, to_field = 'SITL_CODIGO', db_column = 'CLIE_SITUACION_LABORAL')	
    CLNA_EXPIRA_PASAPORTE = models.DateTimeField()
    CLNA_INICIO_RESIDENCIA = models.DateTimeField()
    CLNA_NUM_CARGAS	= models.PositiveIntegerField()		
    CLNA_EMPRESA_TRABAJA = models.CharField(max_length = 60)
    CLNA_INICIO_INGRESOS = models.DateTimeField()

    class Meta:
        db_table = "CLIENTE_NATURAL"

class GrupoEconomico(models.Model):
    GREC_CODIGO = models.PositiveIntegerField(primary_key = True)
    GREC_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "GRUPO_ECONOMICO"

class TipoEmpresa(models.Model):
    TIEM_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIEM_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "TIPO_EMPRESA"

class ClienteJuridico(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField(primary_key = True)		
    TIEM_CODIGO	= models.ForeignKey(TipoEmpresa, on_delete = cascade_delete, db_column = 'TIEM_CODIGO')	
    GREC_CODIGO	= models.ForeignKey(GrupoEconomico, on_delete = cascade_delete, db_column = 'GREC_CODIGO')
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
