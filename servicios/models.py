from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre=models.CharField(max_length=30) 
    imagen=models.ImageField(upload_to='servicios')
    encargado=models.CharField(max_length=30) 
    descripcion=models.CharField(max_length=100) 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="servicio"
        verbose_name_plural="servicio"

    def __str__(self):
        return self.nombre