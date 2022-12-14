from django.urls import re_path as url
from . import views

app_name = "accounts"

urlpatterns = [
    url(r"^crear_cuenta/$", views.crear_cuenta, name = "crear_cuenta"),
    url(r"^iniciar_sesion/$", views.iniciar_sesion, name = "iniciar_sesion"),
    url(r"^cerrar_sesion/$", views.cerrar_sesion, name = "cerrar_sesion"),
]