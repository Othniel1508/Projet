from django.db import models


class Agronome(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    recommandations = models.TextField()

    class Meta:
        db_table = 'agronome'
