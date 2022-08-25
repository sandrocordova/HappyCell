from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework.response import Response
from apps.catalog.models import CiudadCat, ZonaCat, PaisCat, TipoTelefono
from apps.catalog.models import TipoDireccion, TipoEmpresa, TipoClase, TipoProyecto, Profesion, Nacionalidad, ActividadEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral
from apps.catalog.serializer import TipoDireccionSerializer, TipoEmpresaSerializer, TipoClaseSerializer, TipoProyectoSerializer, ProfesionesSerializer, ProfesionesSerializer, NacionalidadSerializer, ActiEconomicaSerializer, TipoRolSerializer, SexoSerializer, ViviendaSerializer, EstadoCivilSerializer, SituacionLaboralCivilSerializer
from apps.catalog.serializer import CiudadSerializerCat, ZonaSerializerCat, PaisSerializerCat, TipoTelefonoSerializer

#Catálogos
class catalog_api_views(APIView):
    def get(self, request):
        catalog_id = ['tipo_telefono','pais','zona','ciudad','tipo_direccion','tipo_empresa','tipo_clase','tipo_proyecto','profesion', 'nacionalidad', 'actividad_economica', 'tipo_rol','sexo', 'vivienda', 'estado_civil', 'situacion_laboral']
        catalog_list =[]
        json_response = {
            'status': True,
            'message': "Response exitoso"
            }
        if 'tipo_telefono' in catalog_id:
            consulta = TipoTelefono.objects.using('clientes').all()
            profesionesSerializer = TipoTelefonoSerializer(consulta, many = True)
            catalog_list.append({'tipo_telefono':profesionesSerializer.data})
        if 'pais' in catalog_id:
            consulta = PaisCat.objects.using('clientes').all()
            profesionesSerializer = PaisSerializerCat(consulta, many = True)
            catalog_list.append({'pais':profesionesSerializer.data})
        if 'zona' in catalog_id:
            consulta = ZonaCat.objects.using('clientes').all()
            profesionesSerializer = ZonaSerializerCat(consulta, many = True)
            catalog_list.append({'zona':profesionesSerializer.data})
        if 'ciudad' in catalog_id:
            consulta = CiudadCat.objects.using('clientes').all()
            profesionesSerializer = CiudadSerializerCat(consulta, many = True)
            catalog_list.append({'ciudad':profesionesSerializer.data})
        if 'tipo_direccion' in catalog_id:
            consulta = TipoDireccion.objects.using('clientes').all()
            profesionesSerializer = TipoDireccionSerializer(consulta, many = True)
            catalog_list.append({'tipo_direccion':profesionesSerializer.data})
        if 'tipo_empresa' in catalog_id:
            consulta = TipoEmpresa.objects.using('clientes').all()
            profesionesSerializer = TipoEmpresaSerializer(consulta, many = True)
            catalog_list.append({'tipo_empresa':profesionesSerializer.data})
        if 'tipo_clase' in catalog_id:
            consulta = TipoClase.objects.using('clientes').all()
            profesionesSerializer = TipoClaseSerializer(consulta, many = True)
            catalog_list.append({'tipo_clase':profesionesSerializer.data})
        if 'tipo_proyecto' in catalog_id:
            consulta = TipoProyecto.objects.using('clientes').all()
            profesionesSerializer = TipoProyectoSerializer(consulta, many = True)
            catalog_list.append({'tipo_proyecto':profesionesSerializer.data})
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

