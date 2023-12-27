from django.shortcuts import render
from .models import Agronome
from django.http import HttpResponseRedirect


def formulaire_agronome(request):
    if request.method == 'POST':
        agronome = Agronome()
        agronome.nom = request.POST.get('nom')
        agronome.adresse = request.POST.get('adresse')
        agronome.telephone = request.POST.get('telephone')
        agronome.recommandations = request.POST.get('recommandations')
        agronome.save()
        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'Agronome.html')
