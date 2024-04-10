from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categoria(models.Model):
    nombre=models.CharField(max_length=30) 
    descripcion=models.CharField(max_length=30, null=True, blank=True) 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.nombre
    

class post(models.Model):
    titulo=models.CharField(max_length=30) 
    imagen=models.ImageField(upload_to='blog', null=True, blank=True )
    contenido=models.CharField(max_length=1500) 
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(categoria)



    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"

    def __str__(self):
        return self.titulo