from django.db import models

class Expediente(models.Model):
    id = models.AutoField(primary_key=True)
    NumEp = models.CharField(max_length=1000)
    Enajenante = models.CharField(max_length=1000)
    Adquiriente = models.CharField(max_length=1000)
    Isai = models.CharField(max_length=1000)
    Isr = models.CharField(max_length=1000)


# Create your models here.
