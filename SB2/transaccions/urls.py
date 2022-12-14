from django.urls import re_path as url
from . import views

app_name = "transaccions"

urlpatterns = [
    url(r"^deposito/$", views.deposito, name = "deposito"),
    url(r"^pago_servicios/$", views.pago_servicios, name = "pago_servicios"),
    url(r"^retiro/$", views.retiro, name = "retiro"),
    url(r"^transferencia_dinero/$", views.transferencia_dinero, name = "transferencia_dinero"),
]