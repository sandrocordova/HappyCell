from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.agencia.models import Agencia


# Create your views here.


def menu(request):
    #AGENCIA = Agencia.objects.raw("SELECT * FROM AGENCIA")
    AGENCIA = Agencia.objects.raw("SELECT AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")[0]
    
    context = {'agencias': AGENCIA}
    print("HIZO LA CONSULTA ----------------------------")
    print(AGENCIA)
    print(context)
    print(Agencia)
    
    print("HIZO LA CONSULTA ---------------------------- FIN")
    return render(request, 'menu.html', context)
