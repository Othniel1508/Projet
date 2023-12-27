from django.urls import path

from . import views

urlpatterns = [
    path('', views.formulaire_veterinaire, name='veterinaire')
]
