from django.shortcuts import render

# Create your views here.


def git(request):
    return render(request,"git.html")

def gem(request):
    return render(request,"gem.html")

def gc(request):
    return render(request,"gc.html")

def tc(request):
    return render(request,"tc.html")
