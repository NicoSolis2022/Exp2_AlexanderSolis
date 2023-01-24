from django.shortcuts import render, redirect
from .models import cliente
from django.contrib import messages
# Create your views here.

def home(request):
   clientesRegistrados = cliente.objects.all()
   messages.succes(request, 'Usuario registrado')
   return render (request, "core/registrarUsuario.html", {"cliente", clientesRegistrados})

def index(request):
    return render(request, 'core/index.html')


def acercade(request):
    return render(request, 'core/acercade.html')


def api(request):
    return render(request, 'core/api.html')


def formulario1(request):
    return render(request, 'core/formulario1.html')


def galeria(request):
    return render(request, 'core/galeria.html')


def Registro2(request):
    return render(request, 'core/Registro2.html') 

def registro3(request):
    return render(request, 'core/registro3.html') 

def registrarUsuario(request):
    nombre = request.POST['nombre']
    email = request.POST['email']
    clave = request.POST['clave']

    cliente = cliente.objets.create(
        nombre=nombre, email=email, clave=clave)
    return redirect('core/registrarUsuario.html')

