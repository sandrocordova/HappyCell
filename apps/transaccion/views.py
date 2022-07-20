from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.transaccion.models import Agencia

# Create your views here.


def menu(request):
    agencia = Agencia.objects.all()
    context = {'agencias': agencia}
    return render(request, 'menu.html', context)
