from django.db import models


class Consommateur(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    preferences_alimentaires = models.TextField()
    retours_produits = models.TextField()
    demande_produits = models.TextField()

    class Meta:
        db_table = 'consommateur'
