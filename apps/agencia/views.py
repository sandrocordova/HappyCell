from django.http import HttpResponse
from apps.agencia.models import Empresa

def menu(request):
    return HttpResponse("Pagina principal django")