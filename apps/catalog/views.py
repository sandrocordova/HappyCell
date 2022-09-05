from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework.response import Response
from apps.catalog.models import CiudadCat, ZonaCat, PaisCat, TipoTelefono, Provincia, Canton, Parroquia, TipoVinculo, TipoObservacion, Profesion
from apps.catalog.models import TipoDireccion, TipoEmpresa, TipoClase, TipoProyecto, Profesion, Nacionalidad, ActividadEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral
from apps.catalog.models import TipoCliente, GrupoEconomico, TipoDocumento, NivelInstruccion
from apps.catalog.serializer import TipoDireccionSerializer, TipoEmpresaSerializer, TipoClaseSerializer, TipoProyectoSerializer, ProfesionesSerializer, NacionalidadSerializer, ActiEconomicaSerializer, TipoRolSerializer, SexoSerializer, ViviendaSerializer, EstadoCivilSerializer, SituacionLaboralCivilSerializer
from apps.catalog.serializer import CiudadSerializerCat, ZonaSerializerCat, PaisSerializerCat, TipoTelefonoSerializer, ProvinciaSerializer
from apps.catalog.serializer import ProvinciaSerializer, CantonSerializer, ParroquiaSerializer, TipoVinculoSerializer, TipoObservacionSerializer
from apps.catalog.serializer import TipoClienteSerializer, GrupoEconomicoSerializer, TipoDocumentoSerializer, NivelInstruccionSerializer


#Catálogos
class catalog_api_views(APIView):
    def get(self, request):
        catalog_id = ['nivel_instruccion','tipo_documento','grupo_economico','tipo_cliente','profesion','tipo_observacion_cliente','tipo_vinculo','provincia','canton','parroquia','tipo_telefono','pais','zona','ciudad','tipo_direccion','tipo_empresa','tipo_clase','tipo_proyecto','profesion', 'nacionalidad', 'actividad_economica', 'tipo_rol','sexo', 'vivienda', 'estado_civil', 'situacion_laboral']
        catalog_list =[]
        json_response = {
            'status': True,
            'message': "Response exitoso"
            }
        if 'nivel_instruccion' in catalog_id:
            consulta = NivelInstruccion.objects.using('clientes').all()
            profesionesSerializer = NivelInstruccionSerializer(consulta, many = True)
            catalog_list.append({'nivel_instruccion':profesionesSerializer.data})
        if 'tipo_documento' in catalog_id:
            consulta = TipoDocumento.objects.using('clientes').all()
            profesionesSerializer = TipoDocumentoSerializer(consulta, many = True)
            catalog_list.append({'tipo_documento':profesionesSerializer.data})
        if 'grupo_economico' in catalog_id:
            consulta = GrupoEconomico.objects.using('clientes').all()
            profesionesSerializer = GrupoEconomicoSerializer(consulta, many = True)
            catalog_list.append({'grupo_economico':profesionesSerializer.data})
        if 'tipo_cliente' in catalog_id:
            consulta = TipoCliente.objects.using('clientes').all()
            profesionesSerializer = TipoClienteSerializer(consulta, many = True)
            catalog_list.append({'tipo_cliente':profesionesSerializer.data})
        if 'tipo_observacion_cliente' in catalog_id:
            consulta = TipoObservacion.objects.using('clientes').all()
            profesionesSerializer = TipoObservacionSerializer(consulta, many = True)
            catalog_list.append({'tipo_observacion_cliente':profesionesSerializer.data})
        if 'tipo_vinculo' in catalog_id:
            consulta = TipoVinculo.objects.using('clientes').all()
            profesionesSerializer = TipoVinculoSerializer(consulta, many = True)
            catalog_list.append({'tipo_vinculo':profesionesSerializer.data})
        if 'provincia' in catalog_id:
            consulta = Provincia.objects.using('clientes').all()
            profesionesSerializer = ProvinciaSerializer(consulta, many = True)
            catalog_list.append({'provincia':profesionesSerializer.data})
        if 'canton' in catalog_id:
            consulta = Canton.objects.using('clientes').all()
            profesionesSerializer = CantonSerializer(consulta, many = True)
            catalog_list.append({'canton':profesionesSerializer.data})
        if 'parroquia' in catalog_id:
            consulta = Parroquia.objects.using('clientes').all()
            for parroquia in consulta:
                parroquia.PROV_CODIGO = int(parroquia.PROV_CODIGO)
                parroquia.CANT_CODIGO = int(parroquia.CANT_CODIGO)
            profesionesSerializer = ParroquiaSerializer(consulta, many = True)
            catalog_list.append({'parroquia':profesionesSerializer.data})
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
