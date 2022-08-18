from django.db import models

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
    
    class Meta:
        db_table = "cliente"