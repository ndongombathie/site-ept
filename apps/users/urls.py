from django.urls import path 
from .views import profil,connexion

urlpatterns = [
    path("profil/",profil,name="profil"),
   
]
