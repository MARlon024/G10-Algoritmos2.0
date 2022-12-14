from django.shortcuts import render, redirect
from . import forms
from . import models
from profiles.models import Estado

#operaciones
def transferencia_dinero(request):
    if request.method == "POST":
        form = forms.TransferenciasForm(request.POST)
        if form.is_valid():
            form.save()
        
            usuario_actual = models.Transferencias.objects.get(ingresar_usuario=request.user)
            numero_cuenta_destino = usuario_actual.ingresar_numero_cuenta_destino

            temp = usuario_actual
            
            usuario_destino = Estado.objects.get(numero_cuenta=numero_cuenta_destino)
            monto_transferencia = usuario_actual.ingresar_monto 
            usuario_actual = Estado.objects.get(nombre_usuario=request.user)

            usuario_actual.dinero = usuario_actual.dinero - monto_transferencia
            usuario_destino.dinero = usuario_destino.dinero + monto_transferencia

            usuario_actual.save()
            usuario_destino.save()

            temp.delete()

        return redirect("perfil.html")
    else:
        form = forms.TransferenciasForm()
    return render(request, "transferencia_dinero.html", {"form": form})

def pago_servicios(request):
    return render(request, "pago_servicios.html")

def retiro(request):
    if request.method == "POST":
        form = forms.Depositos_RetirosForm(request.POST)
        if form.is_valid():
            form.save()

            usuario_actual = models.Depositos_Retiros.objects.get(ingresar_usuario=request.user)

            temp = usuario_actual

            monto_retiro = usuario_actual.ingresar_monto
            usuario_actual = Estado.objects.get(nombre_usuario=request.user)

            usuario_actual.dinero = usuario_actual.dinero - monto_retiro

            usuario_actual.save()

            temp.delete()

        return redirect("perfil.html")
    else:
        form = forms.Depositos_RetirosForm()    
    return render(request, "retiro.html", {"form": form}) 

def deposito(request):
    if request.method == "POST":
        form = forms.Depositos_RetirosForm(request.POST)
        if form.is_valid():
            form.save()

            usuario_actual = models.Depositos_Retiros.objects.get(ingresar_usuario=request.user)

            temp = usuario_actual

            monto_deposito = usuario_actual.ingresar_monto
            usuario_actual = Estado.objects.get(nombre_usuario=request.user)

            usuario_actual.dinero = usuario_actual.dinero + monto_deposito

            usuario_actual.save()

            temp.delete()

        return redirect("perfil.html")
    else:
        form = forms.Depositos_RetirosForm()    
    return render(request, "deposito.html", {"form": form})  