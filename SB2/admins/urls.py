from django.urls import re_path as url
from . import views

app_name = "admins"

urlpatterns = [
    url(r"^$", views.index, name = "admin_index"),
    url(r"^tabla_clientes/$", views.tabla_clientes, name = "tabla_clientes"),
    url(r"^editar_cliente/(?P<id_cliente>\d+)/$", views.editar_cliente, name = "editar_cliente"),
]
