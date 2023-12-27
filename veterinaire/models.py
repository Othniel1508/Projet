from django.db import models


class Veterinaire(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    donnees_sante_animale = models.TextField()

    class Meta:
        db_table = 'veterinaire'
