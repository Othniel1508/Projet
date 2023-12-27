from django.db import models


class Agriculteur(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    capteurs = models.TextField()
    informations = models.TextField()
    statistiques = models.TextField()

    class Meta:
        db_table = 'agriculteur'
