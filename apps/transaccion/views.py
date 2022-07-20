from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.transaccion.models import AGENCIA


# Create your views here.


def menu(request):
    agencia = AGENCIA.objects.all()
    context = {'agencias': agencia}
    print("HIZO LA CONSULTA ----------------------------")
    print(agencia)
    return render(request, 'menu.html', context)
