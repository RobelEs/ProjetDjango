from django.db import models

# Create your models here.

#création class

class Produit(models.Model):
    nom_produit = models.CharField(max_length=20)
    prix_produit = models.DecimalField(max_digits = 20, decimal_places = 0)


