from django.db import models

#CATÁLOGOS
class Profesiones(models.Model):
    prof_codigo = models.PositiveIntegerField(primary_key = True)
    prof_descripcion = models.CharField(max_length=40, null=False)
    
    class Meta:
        db_table = "profesion"
        
class Nacionalidad(models.Model):
    naci_codigo = models.PositiveIntegerField(primary_key = True)
    naci_descripcion = models.CharField(max_length=40, null=False)
    
    class Meta:
        db_table = "nacionalidad"
        
class ActiEconomica(models.Model):
    acti_codigo = models.PositiveIntegerField(primary_key = True)
    acti_descripcion = models.CharField(max_length=40, null=False)
    
    class Meta:
        db_table = "actividad_economica"
        
class TipoRol(models.Model):
    tiro_codigo = models.CharField(max_length=2, primary_key = True)
    tirol_descripcion = models.CharField(max_length=50, null=False)
    
    class Meta:
        db_table = "tipo_rol"
        
class Sexo(models.Model):
    sexo_codigo = models.CharField(max_length=2, primary_key = True)
    sexo_descripcion = models.CharField(max_length=40, null=False)
    
    class Meta:
        db_table = "sexo"
        
class Vivienda(models.Model):
    vivi_codigo = models.PositiveIntegerField(primary_key = True)
    vivi_descripcion = models.CharField(max_length=50, null=False)
    
    class Meta:
        db_table = "vivienda"
        
class EstadoCivil(models.Model):
    esci_codigo = models.PositiveIntegerField(primary_key = True)
    esci_descripcion = models.CharField(max_length=40, null=False)
    
    class Meta:
        db_table = "estado_civil"

class SituacionLaboral(models.Model):
    sitl_codigo = models.PositiveIntegerField(primary_key = True)
    sitl_descripcion = models.CharField(max_length=50, null=False)
    
    class Meta:
        db_table = "situacion_laboral"


#FIN CATALOGOS
