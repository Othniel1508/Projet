from django.urls import path

from . import views

urlpatterns = [
    path('', views.formulaire_transporteur, name='transporteur')
]
