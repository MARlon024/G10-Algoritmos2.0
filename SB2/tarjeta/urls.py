from django.urls import re_path as url
from . import views

app_name = "tarjeta"

urlpatterns = [
    url(r"^bloquear_tarjeta/$", views.bloquear_tarjeta, name = "bloquear_tarjeta"),
    url(r"^estado_tarjeta/$", views.estado_tarjeta, name = "estado_tarjeta"),
    url(r"^crear_tarjeta/$", views.crear_tarjeta, name = "crear_tarjeta"),
]