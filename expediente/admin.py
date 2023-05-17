from django.contrib import admin
from .models import Expediente

admin.site.register(Expediente)


def __str__(self):
        fila = "Ep:" + self.Ep + "Enajenante:" + self.Enajenante + "Adquiriente:" + self.Adquiriente + "ISAI:" + self.isai +"ISR:" + self.isr 
        return fila

def delete(self, using=None, keep_parents = False):
      super().delete()



# Register your models here.
