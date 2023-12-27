from django.db import models


class Transporteur(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    disponibilite_capacite = models.TextField()
    informations_logistiques = models.TextField()
    etats_livraison = models.TextField()

    class Meta:
        db_table = 'transporteur'
