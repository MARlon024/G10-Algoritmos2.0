from django.urls import re_path as url
from . import views

app_name = "profiles"

urlpatterns = [
    url(r"^index_user/$", views.index_user, name = "index_user"),
    url(r"editar_datos/", views.editar_datos, name = "editar_datos"),
    url(r"borrar_cuenta/$", views.borrar_cuenta, name = "borrar_cuenta")
]
