from django.forms import ModelForm

from Projet.models import *


class FrmAjouterProduit(ModelForm):
    class Meta:
        model = Produit
        fields = ["nom_produit", "prix_produit"]
        labels = {
            "nom_produit": "Nom",
            "prix_produit": "Age"
        }
