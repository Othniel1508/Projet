from django.shortcuts import render
from .models import Transporteur
from django.http import HttpResponseRedirect


def formulaire_transporteur(request):
    if request.method == 'POST':
        transporteur = Transporteur()
        transporteur.nom = request.POST.get('nom')
        transporteur.adresse = request.POST.get('adresse')
        transporteur.telephone = request.POST.get('telephone')
        transporteur.disponibilite_capacite = request.POST.get('disponibilite_capacite')
        transporteur.informations_logistiques = request.POST.get('informations_logistiques')
        transporteur.etats_livraison = request.POST.get('etats_livraison')
        transporteur.save()
        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'Transporteur.html')
