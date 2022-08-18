from rest_framework.views import APIView # Procesamiento de Views
from rest_framework import status
from rest_framework.response import Response
from apps.catalog.models import Profesiones, Nacionalidad, ActiEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral
from apps.agencia.api.serializer import ProfesionesSerializer, ProfesionesSerializer, NacionalidadSerializer, ActiEconomicaSerializer, TipoRolSerializer, SexoSerializer, ViviendaSerializer, EstadoCivilSerializer, SituacionLaboralCivilSerializer

#Catálogos
class profesiones_api_views(APIView):
    def get(self, request):
        consulta = Profesiones.objects.using('clientes').all()
        profesionesSerializer = ProfesionesSerializer(consulta, many = True)
        print("Consulta a Profesiones")
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class nacionalidad_api_views(APIView):
    def get(self, request):
        consulta = Nacionalidad.objects.using('clientes').all()
        profesionesSerializer = NacionalidadSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class acti_economica_api_views(APIView):
    def get(self, request):
        consulta = ActiEconomica.objects.using('clientes').all()
        profesionesSerializer = ActiEconomicaSerializer(consulta, many = True)
        print("Consulta a Profesiones")
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class tipo_rol_api_views(APIView):
    def get(self, request):
        consulta = TipoRol.objects.using('clientes').all()
        profesionesSerializer = TipoRolSerializer(consulta, many = True)
        print("Consulta a Profesiones")
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class sexo_api_views(APIView):
    def get(self, request):
        consulta = Sexo.objects.using('clientes').all()
        profesionesSerializer = SexoSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class vivienda_api_views(APIView):
    def get(self, request):
        consulta = Vivienda.objects.using('clientes').all()
        profesionesSerializer = ViviendaSerializer(consulta, many = True)
        print("Consulta a Profesiones")
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
class estado_civil_api_views(APIView):
    def get(self, request):
        consulta = EstadoCivil.objects.using('clientes').all()
        profesionesSerializer = EstadoCivilSerializer(consulta, many = True)
        print("Consulta a Profesiones")
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
class situacion_laboral_api_views(APIView):
    def get(self, request):
        consulta = SituacionLaboral.objects.using('clientes').all()
        profesionesSerializer = SituacionLaboralCivilSerializer(consulta, many = True)
        print("Consulta a Profesiones")
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
#FIN CATALOGOS

