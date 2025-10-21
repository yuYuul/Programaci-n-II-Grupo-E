#from django.http import HttpResponse
#def saludo(request):
    #return HttpResponse("Hola mundo desde Django")
from django.shortcuts import render
def saludor(request):
    return render(request, "index.html")