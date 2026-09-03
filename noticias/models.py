from django.db import models

# Create your models here.
class Noticia(models.Model):
    categoria = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE)
    perfil = models.OneToOneField('Perfil', on_delete=models.CASCADE)

    __str__(self):
        return self.categoria
