from django.db import models

# Create your models here.
class Observacion(models.Model):
    CLIE_CODIGO = models.PositiveIntegerField()
    OBCL_CODIGO = models.PositiveIntegerField(primary_key = True)
    TIOC_CODIGO = models.PositiveIntegerField()
    OBCL_DESCRI = models.CharField(max_length = 4000)

    class Meta:
        db_table = 'OBSERVACION_CLIENTES'
