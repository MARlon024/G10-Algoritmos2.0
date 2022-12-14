from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from profiles.models import Estado
from . import forms
from . import models
import random

#operaciones cuenta user
def generador_numero_cuenta():
    return int(random.uniform(100000, 999999))

def index_user(request):
    try:
        usuario_actual = Estado.objects.get(nombre_usuario=request.user)
    except:
        #si es un nuevo user, creando nuevos datos:
        usuario_actual = Estado()
        usuario_actual.numero_cuenta = generador_numero_cuenta()        
        usuario_actual.dinero = 0
        usuario_actual.nombre_usuario = request.user    
        usuario_actual.save()    
    return render(request, "perfil.html", {"usuario_actual": usuario_actual})    

def editar_datos(request):
    if request.method == "POST":
        #Edición de datos generales para user preexistente
        try:
            usuario_actual = models.DatosGenerales.objects.get(nombre_usuario=request.user)
            form = forms.DatosGeneralesForm(request.POST, instance=usuario_actual)
            if form.is_valid():
                form.save()
        except:
            form = forms.DatosGeneralesForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.nombre_usuario= request.user
                form.save()

        #Cambio de contraseña
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña actualizada.')
            return redirect('change_password')
        else:
            messages.error(request, 'Corrija el error .')

        return redirect("editar_datos.html")
    
    else: # GET(obtener) acciones
        try:
            usuario_actual = models.DatosGenerales.objects.get(nombre_usuario=request.user)
            form1 = forms.DatosGeneralesForm(instance=usuario_actual)
        except:
            form1 = forms.DatosGeneralesForm()

        # Cambio de contraseña
        form2 = PasswordChangeForm(request.user)

        diccionario_forms = {
            "form1": form1,
            "form2": form2
            }  

    return render(request, "editar_datos.html", diccionario_forms)

def borrar_cuenta(request):
    return render(request,"borrar_cuenta.html")

