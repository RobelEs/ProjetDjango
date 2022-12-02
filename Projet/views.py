from django.shortcuts import render
from Projet.models import *
from templates.forms import *


# Create your views here.

def base(request):
    return render(request, "formulaire-Produit.html")


def show_form(request):
    tous_les_produit = Produit.objects.all()
    resultRequete = {"produits": tous_les_produit}
    return render(request, "show.html", resultRequete)


def creeProduit(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prix = request.POST['prix']
        produit = Produit(nom_produit=nom, prix_produit=prix)
        produit.save()
    return render(request, "creerProduit.html")
