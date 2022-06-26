from django.db import models
# Create your models here.

class flia(models.Model):
    
    nombre = models.CharField(max_length = 60)
    
    identificacion = models.IntegerField()
    
    nacionalidad = models.CharField(max_length = 20)
    
    fecha_naci = models.DateField()