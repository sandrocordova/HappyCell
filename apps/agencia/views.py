from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.agencia.models import Agencia


# Create your views here.


def menu(request):
    AGENCIA = Agencia.objects.all("SELECT * FROM AGENCIA")
    context = {'agencias': AGENCIA}
    print("HIZO LA CONSULTA ----------------------------")
    print(AGENCIA)
    return render(request, 'menu.html', context)
