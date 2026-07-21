from django.shortcuts import render

# Create your views here.
def profil(request):
    
    infos = {
        "nom":"Ndongo",
        "prenom":"MBATH",
        "ecole":"EPT",
        "pays":"Sénégal",
        "nationalite":"Sénégalais",
        "connected":False
    }
    
    return render(request, 'profil.html',infos)
   
def connexion(request):
    return render(request,'connexion.html')