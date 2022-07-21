from django.db import models


class Post(models.Model):
    tittle = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
            
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
