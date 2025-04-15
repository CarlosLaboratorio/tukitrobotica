from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {"mensaje":"Bienvenidos a la vista general de nuestros productos"}
    return render(request,"myapp/index.html",contex)