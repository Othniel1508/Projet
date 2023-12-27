from django.shortcuts import render
from .models import Consommateur
from django.http import HttpResponseRedirect

def formulaire_consommateur(request):
    if request.method == 'POST':
        consommateur = Consommateur()
        consommateur.nom = request.POST.get('nom')
        consommateur.adresse = request.POST.get('adresse')
        consommateur.telephone = request.POST.get('telephone')
        consommateur.preferences_alimentaires = request.POST.get('preferences_alimentaires')
        consommateur.retours_produits = request.POST.get('retours_produits')
        consommateur.demande_produits = request.POST.get('demande_produits')
        consommateur.save()
        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'Consommateur.html')
