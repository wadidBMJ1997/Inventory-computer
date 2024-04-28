from django.db import models

# Create your models here.
class Raton(models.Model):
    id= models.CharField(primary_key=True,max_length=6)
    tipoEntrada = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    
    def __str__(self) :
        texto = "{0}({1})"
        return texto.format(self.tipoEntrada, self.marca)

class Teclado(models.Model):
    id= models.CharField(primary_key=True,max_length=6)
    tipoEntrada = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)

    def __str__(self) :
        texto = "{0}({1})"
        return texto.format(self.tipoEntrada, self.marca)

class Monitor(models.Model):
    id= models.CharField(primary_key=True,max_length=6)
    marca = models.CharField(max_length=15)
    tamaño= models.PositiveSmallIntegerField()

    def __str__(self) :
        texto = "{0}({1})"
        return texto.format(self.marca,self.tamaño)

class Computador(models.Model):
    id= models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=15)
    monitor = models.CharField(max_length=15)
    teclado= models.CharField(max_length=15)
    raton = models.CharField(max_length=15)

    def __str__(self) :
        texto = "{0}({1})"
        return texto.format(self.nombre, self.monitor,self.teclado,self.raton,)
    