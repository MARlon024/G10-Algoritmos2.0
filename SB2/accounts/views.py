from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def crear_cuenta(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:iniciar_sesion")
    else:
        form = UserCreationForm()
    return render(request, "crear_cuenta.html", {"form": form})

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profiles:index_user")
    else:
        form = AuthenticationForm()
        return render(request, "iniciar_sesion.html", {"form": form})

def cerrar_sesion(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:iniciar_sesion")
