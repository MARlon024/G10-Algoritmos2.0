from django.shortcuts import render
from profiles.models import DatosGenerales
from profiles import forms
def index(request):
    return render(request, "admin_base.html")

def tabla_clientes(request):
    cliente = DatosGenerales.objects.all()
    clientes = {'clientes':cliente}
    return render(request, "tabla_clientes.html", clientes)

def tabla_historial(request):
    return render(request, "tabla_clientes.html")

def editar_cliente(request, id_cliente):
    cliente = DatosGenerales.objects.get(id = id_cliente)
    if request.method == 'GET':
        form = forms.DatosGeneralesForm(instance=cliente)
    else: 
        form = forms.DatosGeneralesForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('tabla_clientes')
    return render(request, 'editar_cliente.html',{'form':form})