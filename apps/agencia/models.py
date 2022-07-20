from django.db import models


class Agencia(models.Model):
    zona_codigo = models.ForeignKey('Zona', models.DO_NOTHING, db_column='ZONA_CODIGO', primary_key=True)  # Field name made lowercase.
    empr_codigo = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EMPR_CODIGO')  # Field name made lowercase.
    agen_codigo = models.DecimalField(db_column='AGEN_CODIGO', max_digits=4, decimal_places=0)  # Field name made lowercase.
    tiag_codigo = models.ForeignKey('TipoAgencia', models.DO_NOTHING, db_column='TIAG_CODIGO')  # Field name made lowercase.
    agen_descripcion = models.CharField(db_column='AGEN_DESCRIPCION', max_length=40)  # Field name made lowercase.
    agen_direccion = models.CharField(db_column='AGEN_DIRECCION', max_length=80)  # Field name made lowercase.
    agen_responsable = models.CharField(db_column='AGEN_RESPONSABLE', max_length=40)  # Field name made lowercase.
    agen_telefono = models.CharField(db_column='AGEN_TELEFONO', max_length=80)  # Field name made lowercase.
    agen_codigo_super = models.CharField(db_column='AGEN_CODIGO_SUPER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ciud_codigo = models.DecimalField(db_column='CIUD_CODIGO', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
