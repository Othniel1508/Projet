from django.shortcuts import render
from .models import MarcheAgricole
from django.http import HttpResponseRedirect

def formulaire_marcher(request):
    if request.method == 'POST':
        marcher = MarcheAgricole()
        marcher.nom = request.POST.get('nom')
        marcher.adresse = request.POST.get('adresse')
        marcher.telephone = request.POST.get('telephone')
        marcher.informations_prix = request.POST.get('informations_prix')
        marcher.disponibilite_produits = request.POST.get('disponibilite_produits')
        marcher.demande_marche = request.POST.get('demande_marche')
        marcher.save()
        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'MarcheAgricole.html')
