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

class Empresa(models.Model):
    EMPR_CODIGO = models.CharField(primary_key = True, max_length = 10)
    EMP_EMPR_CODIGO = models.CharField(null = True, max_length = 10)
    VELE_CODIGO = models.CharField(max_length = 3)
    TIEM_CODIGO = models.PositiveIntegerField()
    SUTE_CODIGO = models.PositiveIntegerField()
    MONE_CODIGO = models.CharField(max_length = 3)
    EMPR_NOMBRE = models.CharField(max_length = 80)
    EMPR_IDENTIFICACION = models.CharField(max_length = 20)
    EMPR_FECHA_CONSTITUCION = models.DateTimeField()
    EMPR_FECHA_CREACION = models.DateTimeField()
    EMPR_DIRECCION = models.CharField(max_length = 80)
    FECHA_ACTUAL = models.DateTimeField()
    FECHA_ANTERIOR = models.DateTimeField()
    FECHA_SIGUIENTE = models.DateTimeField()
    GREM_CODIGO = models.PositiveIntegerField()
    PERI_CODIGO = models.PositiveIntegerField()
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

class Observacion(models.Model):
    CLIE_CODIGO = models.PositiveIntegerField()
    OBCL_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIOC_CODIGO = models.PositiveIntegerField()
    OBCL_DESCRI = models.CharField(max_length = 4000)

    class Meta:
        db_table = 'OBSERVACION_CLIENTES'

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
        unique_together = (("CLIE_CODIGO", "DIRE_CODIGO", "TIDE_CODIGO"))

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

class BalanceCliente(models.Model):
    CUBA_CUENTA = models.CharField(max_length = 40)
    CLIE_CODIGO = models.PositiveIntegerField(max_length = 10)
    BAEM_FECHA = models.DateTimeField(primary_key = True)
    BAEM_VALOR = models.DecimalField(max_digits = 18, decimal_places = 4)

    class Meta:
        db_table = 'BALANCE_CLIENTE'
        unique_together = ((
            "CUBA_CUENTA", 
            "CLIE_CODIGO", 
            "BAEM_FECHA"
            ))
