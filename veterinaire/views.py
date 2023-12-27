from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Veterinaire


def formulaire_veterinaire(request):
    if request.method == 'POST':
        veterinaire = Veterinaire()
        veterinaire.nom = request.POST.get('nom')
        veterinaire.adresse = request.POST.get('adresse')
        veterinaire.telephone = request.POST.get('telephone')
        veterinaire.donnees_sante_animale = request.POST.get('donnees_sante_animale')
        veterinaire.save()
        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'Veterinaire.html')
# Create your views here.
