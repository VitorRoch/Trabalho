from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def trama(request):
    return render(request,"trama.html")

def atores(request):
    return render(request,"atores.html")

def imagens(request):
    return render(request,"imagens.html")