from django.db import models

# Create your models here.


class cliente(models.Model):
    nombre = models.CharField(primary_key=True,max_length=50)
    email = models.CharField(max_length=100)
    clave = models.CharField(max_length=30)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.email)