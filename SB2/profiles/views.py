from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth import update_session_auth_hash

def generadorID():
    pass

def index_user(request):
    return render(request, "perfil.html")

def editar_datos(request):
    return render(request, "editar_datos.html")

def transferencia_dinero(request):
    return render(request, "transferencia.html")

def pago_online(request):
    return render(request, "pago_servicios.html")

def configuraciones(request):
    return render(request, "configuraciones.html")

def borrar_cuenta(request):
    return render(request,"borrar_cuenta.html")