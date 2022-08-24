from django.db import models

# Create your models here.
cascade_delete = models.CASCADE

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
    TIAS_CODIGO = models.PositiveIntegerField(primary_key = True)
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
    PAIS_CODIGO = models.CharField(max_length = 3)
    VELE_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'VEHICULO_LEGAL'

class TipoEmpresa(models.Model):
    TIEM_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIEM_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_EMPRESA'

class SubtipoEmpresa(models.Model):
    TIEM_CODIGO = models.PositiveIntegerField()
    SUTE_CODIGO = models.PositiveIntegerField(primary_key = True)
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
    PERI_CODIGO = models.PositiveIntegerField(primary_key = True)
    PERI_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'PERIOCIDAD'

class GrupoEconomico(models.Model):
    GREC_CODIGO = models.PositiveIntegerField(primary_key = True)
    GREC_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = "GRUPO_ECONOMICO"

class Zona(models.Model):
    ZONA_CODIGO = models.PositiveIntegerField(primary_key = True)
    PAIS_CODIGO = models.PositiveIntegerField()
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
    TIBA_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIBA_DESCRIPCION = models.CharField(max_length = 40)
    TIBA_RESPONSABLE = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_DE_BANCA'

class TipoAgencia(models.Model):
    TIAG_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIAG_DESCRIPCION = models.CharField(max_length = 40)
    TIAG_CENTRO_CANJE = models.CharField(max_length = 2
    )
    class Meta:
        db_table = 'TIPO_AGENCIA'

class Agencia(models.Model):
    ZONA_CODIGO = models.PositiveIntegerField()
    EMPR_CODIGO = models.PositiveIntegerField()
    AGEN_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIAG_CODIGO = models.PositiveIntegerField()
    AGEN_DESCRIPCION = models.CharField(max_length = 40)
    AGEN_DIRECCION = models.CharField(max_length = 40)
    AGEN_RESPONSABLE = models.CharField(max_length = 40)
    AGEN_TELEFONO = models.CharField(max_length = 40)
    AGEN_CODIGO_SUPER = models.CharField(max_length = 40, null = True)
    CIUD_CODIGO = models.PositiveIntegerField()

    class Meta:
        db_table = 'AGENCIA'

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

class TipoCuentaBalance(models.Model):
    TICB_CODIGO = models.PositiveIntegerField(primary_key = True)
    TICB_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_CUENTA_BALANCE'

class CuentaBalance(models.Model):
    CUBA_CUENTA = models.PositiveBigIntegerField(primary_key = True)
    TICB_CODIGO = models.PositiveIntegerField()
    CUBA_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'CUENTA_BALANCE'

class TipoObservacion(models.Model):
    TIOC_CODIGO = models.AutoField(primary_key = True)
    TIOC_DESCRI = models.CharField(max_length = 40)
    TIOC_CAMBIO = models.PositiveIntegerField()

    class Meta:
        db_table = 'TIPO_OBSERVACION_CLIENTE'

class TipoDireccion(models.Model):
    TIDE_CODIGO = models.AutoField(primary_key = True)
    TIDE_DESCRIPCION = models.CharField(max_length = 40)
    class Meta:
        db_table = 'TIPO_DIRECCION'

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

class TipoTelefono(models.Model):
    TITE_CODIGO = models.AutoField(primary_key = True)
    TITE_DESCRIPCION = models.CharField(max_length = 40)

    class Meta:
        db_table = 'TIPO_TELEFONO'

class TipoProyecto(models.Model):
    COD_TIPO_PROYECTO = models.PositiveIntegerField(primary_key = True)
    DESC_TIPO_PROYECTO = models.CharField(max_length =	50, null = True)

    class Meta:
        db_table = 'CLIE_TIPO_PROYECTO'

class TipoRol(models.Model):
    TIRO_CODIGO = models.CharField(max_length = 2, primary_key = True)
    TIROL_DESCRIPCION = models.CharField(max_length = 50)

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
