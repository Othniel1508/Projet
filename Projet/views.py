from django.shortcuts import render


def connect(request):
    return render(request, 'connexion.html')


def agriculteur(request):
    return render(request, 'Agricultueur.html')


def agronome(request):
    return render(request, 'Agronome.html')


def consommateur(request):
    return render(request, 'Consommateur.html')


def marcher(request):
    return render(request, 'MarcheAgricole.html')


def transporteur(request):
    return render(request, 'Transporteur.html')


def veterinaire(request):
    return render(request, 'Veterinaire.html')
