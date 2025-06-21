from django.db import models

# Create your models here.
class Aeropuerto(models.Model):
    id_aeropuerto = models.AutoField(primary_key=True)
    nombre_a = models.CharField(max_length=100)      
    direccion_a = models.CharField(max_length=200)    
    ciudad_a = models.CharField(max_length=100)       
    pais_a = models.CharField(max_length=100)        
    num_pista = models.IntegerField()                 
    telefono = models.CharField(max_length=20)    

    def __str__(self):
        return self.nombre_a