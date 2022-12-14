from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from tarjeta.models import Tarjeta
from profiles import forms
from profiles import models

#operaciones tarjeta
def crear_tarjeta(request):
    return render(request, "tarjeta_base.html")

def bloquear_tarjeta(request):
    return render(request, "tarjeta_base.html")

def estado_tarjeta(request):
    return render(request, "tarjeta_base.html")
