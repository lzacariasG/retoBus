from django.db import models

# Create your models here.

class registroCSv( models.Model ):
    cliente = models.CharField(max_length=50, null=False)
    contrato = models.CharField(max_length=20, null=False)
    fchCompra = models.CharField(max_length=11, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    empresa = models.CharField(max_length=50, null=False)
    valorAdeudo = models.CharField(max_length=20 , null=False)
    nmArchivo = models.CharField(max_length=20, null=False, default='prueba.csv')

    def __str__(self):
        return self.cliente