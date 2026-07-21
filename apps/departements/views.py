from django.shortcuts import render

# Create your views here.

departement=[
    {"nom":"departement genie informatique",
     "diplome":False,
     "listeClass":[
         {"nom":"Fatou","prenom":"Camara"},
         {"nom":"Fatou","prenom":"Camara"},
         {"nom":"Fatou","prenom":"Camara"},
         {"nom":"Fatou","prenom":"Camara"},
         {"nom":"Fatou","prenom":"Camara"},
      ]
    }
]

def git(request):
    context={}
    context = departement[0]
    print(context)
    return render(request,"git.html",context=context)

def gem(request):
    return render(request,"gem.html")

def gc(request):
    return render(request,"gc.html")

def tc(request):
    return render(request,"tc.html")
