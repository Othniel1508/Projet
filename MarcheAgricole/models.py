from django.db import models

class MarcheAgricole(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    informations_prix = models.TextField()
    disponibilite_produits = models.TextField()
    demande_marche = models.TextField()

    class Meta:
        db_table = 'marche_agricole'


