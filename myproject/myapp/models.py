from django.db import models
  

class Departamento(models.Model):

    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2)
    
    
class Empleado(models.Model):
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
