from django.urls import re_path as url
from . import views

app_name = "accounts"

urlpatterns = [
    url(r"^register/$", views.crear_cuenta, name = "signup"),
    url(r"^login/$", views.iniciar_sesion, name = "signin"),
    url(r"^logout/$", views.cerrar_sesion, name = "logout"),
]