from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework.response import Response
from apps.catalog.models import Profesion, Nacionalidad, ActividadEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral
from apps.catalog.serializer import ProfesionesSerializer, ProfesionesSerializer, NacionalidadSerializer, ActiEconomicaSerializer, TipoRolSerializer, SexoSerializer, ViviendaSerializer, EstadoCivilSerializer, SituacionLaboralCivilSerializer

#Catálogos
class catalog_api_views(APIView):
    def get(self, request):
        catalog_id = ['profesion', 'nacionalidad', 'actividad_economica', 'sexo', 'vivienda', 'estado_civil', 'situacion_laboral']
        catalog_list =[]
        json_response = {
            'status': True,
            'message': "Response exitoso"
            }
        if 'profesion' in catalog_id:
            consulta = Profesion.objects.using('clientes').all()
            profesionesSerializer = ProfesionesSerializer(consulta, many = True)
            catalog_list.append({'profesion':profesionesSerializer.data})
        if 'nacionalidad' in catalog_id:
            consulta = Nacionalidad.objects.using('clientes').all()
            nacionalidadSerializer = NacionalidadSerializer(consulta, many = True)
            catalog_list.append({'nacionalidad':nacionalidadSerializer.data})
        if 'actividad_economica' in catalog_id:
            consulta = ActividadEconomica.objects.using('clientes').all()
            actiEconomicaSerializer = ActiEconomicaSerializer(consulta, many = True)
            catalog_list.append({'actividad_economica':actiEconomicaSerializer.data})
        if 'tipo_rol' in catalog_id:
            consulta = TipoRol.objects.using('clientes').all()
            tipoRolSerializer = TipoRolSerializer(consulta, many = True)
            catalog_list.append({'tipo_rol':tipoRolSerializer.data})
        if 'sexo' in catalog_id:
            consulta = Sexo.objects.using('clientes').all()
            sexoSerializer = SexoSerializer(consulta, many = True)
            catalog_list.append({'sexo':sexoSerializer.data})
        if 'vivienda' in catalog_id:
            consulta = Vivienda.objects.using('clientes').all()
            viviendaSerializer = ViviendaSerializer(consulta, many = True)
            catalog_list.append({'vivienda':viviendaSerializer.data})
        if 'estado_civil' in catalog_id:
            consulta = EstadoCivil.objects.using('clientes').all()
            estadoCivilSerializer = EstadoCivilSerializer(consulta, many = True)
            catalog_list.append({'estado_civil':estadoCivilSerializer.data})
        if 'situacion_laboral' in catalog_id:
            consulta = SituacionLaboral.objects.using('clientes').all()
            situLaboralSerializer = SituacionLaboralCivilSerializer(consulta, many = True)
            catalog_list.append({'situacion_laboral':situLaboralSerializer.data})
        
        json_response['data']=catalog_list
        return Response(json_response)
    
    
    
class profesiones_api_views(APIView):
    def get(self, request):
        consulta = Profesion.objects.using('clientes').all()
        profesionesSerializer = ProfesionesSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class nacionalidad_api_views(APIView):
    def get(self, request):
        consulta = Nacionalidad.objects.using('clientes').all()
        profesionesSerializer = NacionalidadSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class acti_economica_api_views(APIView):
    def get(self, request):
        consulta = ActividadEconomica.objects.using('clientes').all()
        profesionesSerializer = ActiEconomicaSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
    
class tipo_rol_api_views(APIView):
    def get(self, request):
        consulta = TipoRol.objects.using('clientes').all()
        profesionesSerializer = TipoRolSerializer(consulta, many = True)
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
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
class estado_civil_api_views(APIView):
    def get(self, request):
        consulta = EstadoCivil.objects.using('clientes').all()
        profesionesSerializer = EstadoCivilSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
class situacion_laboral_api_views(APIView):
    def get(self, request):
        consulta = SituacionLaboral.objects.using('clientes').all()
        profesionesSerializer = SituacionLaboralCivilSerializer(consulta, many = True)
        return Response(profesionesSerializer.data, status = status.HTTP_200_OK)
#FIN CATALOGOS

