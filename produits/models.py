from django.db import models

# Create your models here.

class Produit(models.Model):
    libelle = models.CharField(max_length=32)
    pu = models.IntegerField()
    qte = models.IntegerField()
    seuil = models.IntegerField()
    def __str__(self):
        return self.libelle