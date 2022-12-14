from django.urls import re_path as url
from . import views

app_name = "profiles"

urlpatterns = [
    url(r"^index_user/$", views.index_user, name = "index_user"),
    url(r"^transferencia/", views.transferencia_dinero, name = "transferencia_dinero"),
    url(r"^pago_servicios/$", views.pago_online, name = "pago_online"),
    url(r"settings/$", views.configuraciones, name = "settings"),
    url(r"edit_details/", views.editar_datos, name = "editar_datos"),
    url(r"delete_account/$", views.borrar_cuenta, name = "borrar_cuenta")
]
