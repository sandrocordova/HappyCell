from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.transaccion.models import AGENCIAS


# Create your views here.


def menu(request):
    AGENCIA = AGENCIAS.objects.all()
    context = {'agencias': AGENCIA}
    print("HIZO LA CONSULTA ----------------------------")
    print(AGENCIA)
    return render(request, 'menu.html', context)
