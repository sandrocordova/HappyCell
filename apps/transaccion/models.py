from django.db import models

# Create your models here.
class AGENCIA(models.Model):
    AGEN_DESCRIPCION = models.CharField(max_length=40)
    AGEN_DIRECCION = models.CharField(max_length=80)
    AGEN_RESPONSABLE = models.CharField(max_length=40)
    AGEN_TELEFONO = models.CharField(max_length=80)