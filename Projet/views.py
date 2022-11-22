from django.shortcuts import render

# Create your views here.

def base(request):

    return render(request, "formulaire-Produit.html")

def show_form(request):

    return  render(request,"show.html")

