from django.shortcuts import render
from .models import Agriculteur
from django.http import HttpResponseRedirect

def formulaire(request):
    if request.method == 'POST':
        agriculteur = Agriculteur()
        agriculteur.nom = request.POST.get('nom')
        agriculteur.adresse = request.POST.get('adresse')
        agriculteur.telephone = request.POST.get('telephone')
        agriculteur.capteurs = request.POST.get('capteurs')
        agriculteur.informations = request.POST.get('informations')
        agriculteur.statistiques = request.POST.get('statistiques')
        agriculteur.save()
        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'Agricultueur.html')
