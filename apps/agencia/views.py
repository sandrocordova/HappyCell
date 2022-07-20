from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.agencia.models import Agencia


# Create your views here.


def menu(request):
    #AGENCIA = Agencia.objects.raw("SELECT * FROM AGENCIA")
    #AGENCIA = Agencia.objects.raw("SELECT AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")[0]
    #AGENCIA = Agencia.objects.raw("SELECT 1 as id AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")
    #entrada = Agencia.objects.raw("SELECT AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")
    entrada = Agencia.objects.raw("SELECT PK_AGENCIA, AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM [SEGURIDAD_APP].[dbo].[AGENCIA]")
    for s in Agencia.objects.raw("SELECT PK_AGENCIA, AGEN_CODIGO, AGEN_DESCRIPCION, AGEN_DIRECCION, AGEN_RESPONSABLE, AGEN_TELEFONO, AGEN_CODIGO_SUPER, CIUD_CODIGO FROM AGENCIA"):
        print(s)
    
    context = {'agencias': entrada}
    print("HIZO LA CONSULTA ----------------------------")
    print(entrada)
    print(context)
    print(connection.queries)
    
    print("HIZO LA CONSULTA ---------------------------- FIN")
    return render(request, 'menu.html', context)
