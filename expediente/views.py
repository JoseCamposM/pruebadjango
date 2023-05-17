from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expediente
from .form import ExpForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def expedientes(request):
    expedientes = Expediente.objects.all()
    return render(request, 'expedientes/index.html', {'expedientes': expedientes})


def crearExpediente(request):
    formulario = ExpForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect(expedientes)

    return render(request, 'expedientes/crear.html', {'formulario': formulario} )


def editarExpediente(request, id):
    expediente = Expediente.objects.get(id=id)
    formulario = ExpForm(request.POST or None, request.FILES or None, instance=expediente)
    if formulario.is_valid() and request.POST:
        formulario.save()

    return render(request, 'expedientes/editar.html', {'formulario': formulario})


def eliminar(request, id):
    expediente = Expediente.objects.get(id = id)
    expediente.delete()
    return redirect('expedientes')




# Create your views here.
