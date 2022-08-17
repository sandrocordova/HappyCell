from django.db import models

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