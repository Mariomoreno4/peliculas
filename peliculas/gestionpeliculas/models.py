from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    usuario=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    
    def __str__(self) :
        
        return self.usuario
    
    
class libros(models.Model):
    autor=models.CharField(max_length=100)
    nombrelibro=models.CharField(max_length=100)
    
    def __str__(self) :
            
        return self.autor
    
        
    