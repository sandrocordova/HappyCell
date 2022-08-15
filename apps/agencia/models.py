
from django.db import models


class Post(models.Model):
    tittle = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    
class Cliente(models.Model):
    CLIE_CODIGO	= models.PositiveIntegerField(db_column='CLIE_CODIGO', primary_key = True)	
    NACI_CODIGO	= models.PositiveIntegerField(db_column='NACI_CODIGO')
    TICL_CODIGO	= models.CharField(db_column='TICL_CODIGO', max_length = 2)
    TIDO_CODIGO	= models.CharField(db_column='TIDO_CODIGO', max_length = 2)
    ACTI_CODIGO	= models.PositiveIntegerField(db_column='ACTI_CODIGO')
    ASES_CODIGO	= models.PositiveIntegerField(db_column='ASES_CODIGO')
    CLIE_IDENTIFICACION	= models.CharField(db_column='CLIE_IDENTIFICACION', max_length =	20)
    CLIE_NOMBRE	= models.CharField(db_column='CLIE_NOMBRE', max_length =	60)
    CLIE_FECHA_CREACION	= models.DateTimeField(db_column='CLIE_FECHA_CREACION')	
    CLIE_NOMBRE_CORRESPONDENCIA	= models.CharField(db_column='CLIE_NOMBRE_CORRESPONDENCIA', max_length =	40)
    clie_estado	= models.CharField(db_column='clie_estado', max_length =	1)
    TISB_CODIGO	= models.PositiveIntegerField(db_column='TISB_CODIGO')	
    clie_tipo = models.CharField(db_column='clie_tipo', max_length = 1)
    CLIE_CLAVE = models.CharField(db_column='CLIE_CLAVE', max_length = 20)
    CLIE_TIPO_ROL = models.CharField(db_column='CLIE_TIPO_ROL', max_length = 2)
    CLIE_TIPO_PROYECTO = models.PositiveIntegerField(db_column='CLIE_TIPO_PROYECTO')	
    comodin	= models.PositiveIntegerField(db_column='comodin')	
    ASES = models.PositiveIntegerField(db_column='ASES')	
    CLIE_FECHA_INACTIVACION	= models.DateTimeField(db_column='CLIE_FECHA_INACTIVACION')	
    CLIE_FECHA_DESAFILIACION = models.DateTimeField(db_column='CLIE_FECHA_DESAFILIACION')	
    sect_codigo	= models.CharField(db_column='sect_codigo', max_length =	5)
    pais_codigo	= models.CharField(db_column='pais_codigo', max_length =	3)
    prov_codigo	= models.CharField(db_column='prov_codigo', max_length =	3)
    cant_codigo	= models.CharField(db_column='cant_codigo', max_length =	5)
    parr_codigo	= models.CharField(db_column='parr_codigo', max_length =	5)
    
            
class Usernav(models.Model):
    usua_login = models.CharField(db_column='USUA_LOGIN', primary_key=True, max_length=40)  # Field name made lowercase.
    usua_nombre = models.CharField(db_column='USUA_NOMBRE', max_length=40)  # Field name made lowercase.
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', max_length=40)  # Field name made lowercase.
    empr_nombre = models.CharField(db_column='EMPR_NOMBRE', max_length=40)  # Field name made lowercase.
    empr_imagen = models.CharField(db_column='EMPR_IMAGEN', max_length=40)  # Field name made lowercase.
    empr_identificacion = models.CharField(db_column='EMPR_IDENTIFICACION', max_length=40)  # Field name made lowercase.
    agen_codigo = models.CharField(db_column='AGEN_CODIGO', max_length=40)  # Field name made lowercase.
    zona_codigo = models.CharField(db_column='ZONA_CODIGO', max_length=40)  # Field name made lowercase.
    cetc_codigo = models.CharField(db_column='CETC_CODIGO', max_length=40)  # Field name made lowercase.
    zona_descripcion = models.CharField(db_column='ZONA_DESCRIPCION', max_length=40)  # Field name made lowercase.
    agen_descripcion = models.CharField(db_column='AGEN_DESCRIPCION', max_length=40)  # Field name made lowercase.
    cetc_descripcion = models.CharField(db_column='CETC_DESCRIPCION', max_length=40)  # Field name made lowercase.
    tipe_codigo = models.CharField(db_column='TIPE_CODIGO', max_length=40)  # Field name made lowercase.
    tipe_descripcion = models.CharField(db_column='TIPE_DESCRIPCION', max_length=40)  # Field name made lowercase.
    
class Usernavtres(models.Model):
    usua_login = models.CharField(db_column='USUA_LOGIN', max_length=200)  # Field name made lowercase.
    tipe_codigo = models.IntegerField(db_column='tipe_codigo')  # Field name made lowercase.
    tipe_descripcion = models.CharField(db_column='TIPE_DESCRIPCION', max_length=200)  # Field name made lowercase.
    mosi_codigo = models.IntegerField(db_column='mosi_codigo')  # Field name made lowercase.
    opme_descripcion = models.CharField(db_column='OPME_DESCRIPCION', max_length=200)  # Field name made lowercase.
    opme_orden = models.IntegerField(db_column='OPME_ORDEN')  # Field name made lowercase.
    opme_codigo = models.IntegerField(db_column='OPME_CODIGO')  # Field name made lowercase.
    vent_codigo = models.IntegerField(db_column='VENT_CODIGO', primary_key=True)  # Field name made lowercase.
    vent_descripcion = models.CharField(db_column='VENT_DESCRIPCION', max_length=200)  # Field name made lowercase.
    vent_ventana = models.CharField(db_column='VENT_VENTANA', max_length=200)  # Field name made lowercase.
    
class Usernavdos(models.Model):
    usua_login = models.CharField(db_column='u.USUA_LOGIN', max_length=40)  # Field name made lowercase.
    usua_nombre = models.CharField(db_column='u.USUA_NOMBRE', max_length=40)  # Field name made lowercase.
    empr_codigo = models.CharField(db_column='ua.EMPR_CODIGO', max_length=40)  # Field name made lowercase.
    empr_nombre = models.CharField(db_column='e.EMPR_NOMBRE', max_length=40)  # Field name made lowercase.
    empr_imagen = models.CharField(db_column='e.EMPR_IMAGEN', max_length=40)  # Field name made lowercase.
    empr_identificacion = models.CharField(db_column='e.EMPR_IDENTIFICACION', max_length=40)  # Field name made lowercase.
    agen_codigo = models.CharField(db_column='ucd.AGEN_CODIGO', max_length=40)  # Field name made lowercase.
    zona_codigo = models.CharField(db_column='ucd.ZONA_CODIGO', max_length=40)  # Field name made lowercase.
    cetc_codigo = models.CharField(db_column='ucd.CETC_CODIGO', max_length=40)  # Field name made lowercase.
    zona_descripcion = models.CharField(db_column='z.ZONA_DESCRIPCION', max_length=40)  # Field name made lowercase.
    agen_descripcion = models.CharField(db_column='a.AGEN_DESCRIPCION', max_length=40)  # Field name made lowercase.
    cetc_descripcion = models.CharField(db_column='cdc.CETC_DESCRIPCION', max_length=40)  # Field name made lowercase.
    tipe_codigo = models.CharField(db_column='ms.TIPE_CODIGO', max_length=40)  # Field name made lowercase.
    tipe_descripcion = models.CharField(db_column='tp.TIPE_DESCRIPCION', max_length=40)  # Field name made lowercase.
    
    
    
class Agencia(models.Model):
    agen_codigo = models.DecimalField(db_column='AGEN_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    agen_descripcion = models.CharField(db_column='AGEN_DESCRIPCION', max_length=40)  # Field name made lowercase.
    agen_direccion = models.CharField(db_column='AGEN_DIRECCION', max_length=80)  # Field name made lowercase.
    agen_responsable = models.CharField(db_column='AGEN_RESPONSABLE', max_length=40)  # Field name made lowercase.
    agen_telefono = models.CharField(db_column='AGEN_TELEFONO', max_length=80)  # Field name made lowercase.
    agen_codigo_super = models.CharField(db_column='AGEN_CODIGO_SUPER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ciud_codigo = models.DecimalField(db_column='CIUD_CODIGO', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

class Empresa(models.Model):
    empr_codigo = models.CharField(db_column='EMPR_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    empr_nombre = models.CharField(db_column='EMPR_NOMBRE', max_length=80)  # Field name made lowercase.
    empr_identificacion = models.CharField(db_column='EMPR_IDENTIFICACION', max_length=20)  # Field name made lowercase.
    empr_fecha_constitucion = models.DateTimeField(db_column='EMPR_FECHA_CONSTITUCION')  # Field name made lowercase.
    empr_fecha_creacion = models.DateTimeField(db_column='EMPR_FECHA_CREACION')  # Field name made lowercase.
    empr_direccion = models.CharField(db_column='EMPR_DIRECCION', max_length=80)  # Field name made lowercase.
    fecha_actual = models.DateTimeField(db_column='FECHA_ACTUAL')  # Field name made lowercase.
    fecha_anterior = models.DateTimeField(db_column='FECHA_ANTERIOR')  # Field name made lowercase.
    fecha_siguiente = models.DateTimeField(db_column='FECHA_SIGUIENTE')  # Field name made lowercase.
    fecha_cierre = models.DateTimeField(db_column='FECHA_CIERRE', blank=True, null=True)  # Field name made lowercase.
    empr_vigente = models.CharField(db_column='EMPR_VIGENTE', max_length=1)  # Field name made lowercase.
    empr_periocidad = models.DecimalField(db_column='EMPR_PERIOCIDAD', max_digits=2, decimal_places=0)  # Field name made lowercase.
    empr_codigo_super = models.CharField(db_column='EMPR_CODIGO_SUPER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empr_rep_legal = models.CharField(max_length=50, blank=True, null=True)
    empr_cargo = models.CharField(max_length=30, blank=True, null=True)
    autorizacion_sri = models.CharField(max_length=30, blank=True, null=True)
    contribuyente_esp = models.CharField(max_length=50, blank=True, null=True)
    empr_fecha_emision = models.CharField(max_length=30, blank=True, null=True)
    empr_imprime_imagen = models.IntegerField(db_column='EMPR_IMPRIME_IMAGEN', blank=True, null=True)  # Field name made lowercase.
    empr_imagen = models.CharField(db_column='EMPR_IMAGEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
