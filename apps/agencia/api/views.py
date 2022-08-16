from urllib import response
from rest_framework.views import APIView # Procesamiento de Views

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from apps.agencia.models import Empresa, Usernav, Usernavdos, Usernavtres, Cliente
from apps.agencia.models import Profesiones, Nacionalidad, ActiEconomica, TipoRol, Sexo, Vivienda, EstadoCivil, SituacionLaboral

from apps.agencia.api.serializer import PostSerializer, UserNavSerializer, UserNavSerializerDos, ClienteSerializer, ProfesionesSerializer
from apps.agencia.api.serializer import ClienteSerializer, ProfesionesSerializer, NacionalidadSerializer, ActiEconomicaSerializer, TipoRolSerializer, SexoSerializer, ViviendaSerializer, EstadoCivilSerializer, SituacionLaboralCivilSerializer



@api_view(['GET'])
def cliente_api_view(request):
    
    if request.method == 'GET':
        clientes = Cliente.objects.using('clientes').all()[4378:4450]
        print(clientes)
        for cliente in clientes:
            if cliente.TICL_CODIGO == "N":
                cliente.TICL_CODIGO = "Natural"
            else:
                cliente.TICL_CODIGO = "Juridico"
        
        serializer_cliente = ClienteSerializer(clientes, many = True)
        print("Consulta a clientes")
        return Response(serializer_cliente.data, status = status.HTTP_200_OK)

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

@api_view(['GET'])
def cliente_api_views(request):
    
    if request.method == 'GET':
        
        consulta = Cliente.objects.using("clientes").raw("select CLIE_CODIGO, NACI_CODIGO, TICL_CODIGO, TIDO_CODIGO, ACTI_CODIGO, ASES_CODIGO, CLIE_IDENTIFICACION, CLIE_NOMBRE, CLIE_FECHA_CREACION, CLIE_NOMBRE_CORRESPONDENCIA, clie_estado, TISB_CODIGO, clie_tipo, CLIE_TIPO_ROL, CLIE_TIPO_PROYECTO, comodin, ASES, CLIE_FECHA_INACTIVACION, CLIE_FECHA_DESAFILIACION, sect_codigo, pais_codigo, prov_codigo, cant_codigo, parr_codigo from cliente")
        
        serializer_cliente = ClienteSerializer(consulta, many = True)
        print(serializer_cliente.data)
        return Response(serializer_cliente.data, status = status.HTTP_200_OK)
    
@api_view(['GET'])
def usernav_api_view(request):
    
    if request.method == 'GET':
        consulta = Usernav.objects.raw("SELECT u.USUA_LOGIN, u.USUA_NOMBRE, ua.EMPR_CODIGO, e.EMPR_NOMBRE, e.EMPR_IMAGEN, e.EMPR_IDENTIFICACION, ucd.AGEN_CODIGO, ucd.ZONA_CODIGO, ucd.CETC_CODIGO, z.ZONA_DESCRIPCION, a.AGEN_DESCRIPCION, cdc.CETC_DESCRIPCION, ms.TIPE_CODIGO, tp.TIPE_DESCRIPCION from  usuario u inner join usuario_empresa ua on u.USUA_CODIGO=ua.USUA_CODIGO  inner join EMPRESA e on ua.EMPR_CODIGO=e.EMPR_CODIGO inner join USUARIO_CENTRO_DE_COSTO ucd on u.USUA_CODIGO=ucd.USUA_CODIGO inner join zona z on ucd.ZONA_CODIGO=z.ZONA_CODIGO inner join agencia a on ucd.AGEN_CODIGO = a.AGEN_CODIGO inner join CENTRO_DE_COSTO cdc on ucd.CETC_CODIGO = cdc.CETC_CODIGO inner join usuario_modulo ms on u.USUA_CODIGO = ms.usua_codigo inner join tipo_perfil tp on ms.TIPE_CODIGO = tp.TIPE_CODIGO where u.USUA_login='ADMINISTRADOR' and ms.MOSI_CODIGO= 1")
        serializer_empresas = UserNavSerializer(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
@api_view(['GET'])
def nav_infor_api_view(request):
    
    if request.method == 'GET':
        consulta = Usernavtres.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION, ve.vent_ventana FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO= tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO = om.MOSI_CODIGO inner join perfil_ventana pf on (om.opme_codigo = pf.OPME_CODIGO) inner join ventana ve ON (PF.VENT_CODIGO=VE.VENT_CODIGO and vent_ventana like '/%%') WHERE u.USUA_CODIGO = 'ADMINISTRADOR' and um.MOSI_CODIGO in (4,8,10) AND OM.OPME_CODIGO >= 800 order by om.opme_orden")  
        serializer_empresas = UserNavSerializerDos(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
    
"""@api_view(['GET'])
def nav_infor_api_view(request):

    if request.method == 'GET':
        consulta = Usernavtres.objects.raw("SELECT TOP 40 u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO=tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO=om.MOSI_CODIGO inner join perfil_ventana pf on um.MOSI_CODIGO=pf.MOSI_CODIGO inner join ventana ve ON PF.VENT_CODIGO=VE.VENT_CODIGO WHERE u.USUA_CODIGO='ADMINISTRADOR' and um.MOSI_CODIGO in (10)")  
        serializer_empresas = UserNavSerializerDos(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def nav_infor_api_view(request):
    
    if request.method == 'GET':
        consulta = Usernavtres.objects.raw("SELECT u.USUA_LOGIN, um.tipe_codigo, tp.TIPE_DESCRIPCION, um.mosi_codigo, OM.OPME_DESCRIPCION, OM.OPME_ORDEN, OM.OPME_CODIGO, pf.VENT_CODIGO, VE.VENT_DESCRIPCION FROM usuario_modulo um inner join usuario u on um.USUA_CODIGO=u.usua_codigo inner join tipo_perfil tp on um.TIPE_CODIGO=tp.TIPE_CODIGO inner join OPCION_MENU om on um.MOSI_CODIGO=om.MOSI_CODIGO inner join perfil_ventana pf on um.MOSI_CODIGO=pf.MOSI_CODIGO inner join ventana ve ON PF.VENT_CODIGO=VE.VENT_CODIGO WHERE ve.VENT_DESCRIPCION like 'WEB%%' AND u.USUA_CODIGO='ADMINISTRADOR' and um.MOSI_CODIGO in (4,8,10) and om.OPME_DESCRIPCION like 'WEB%%' AND PF.VENT_CODIGO like '8%%'")  
        serializer_empresas = UserNavSerializerDos(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
"""
#Detalles de un elementos
@api_view(['GET'])
def detail_view_set(request, pk=None):
    
    if request.method == 'GET':
        #Script que retorne un elemento
        consulta = Empresa.objects.raw("SELECT EMPR_CODIGO, EMPR_NOMBRE, EMPR_IDENTIFICACION FROM [SEGURIDAD_APP].[dbo].[EMPRESA]")  
        #Buscar entre una lista al elemento
        consulta = Empresa.objects.filter(id = pk).first()  
        serializer_empresas = PostSerializer(consulta)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
  
#Listar y guardar  
@api_view(['GET','POST'])
def PostApiViewSet_Post(request):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer_empresas = PostSerializer(data = request.data)
        if serializer_empresas.isValid():
            serializer_empresas.save()
            return Response(serializer_empresas.data, status = status.HTTP_200_OK)
        return Response(serializer_empresas.errors, status = status.HTTP_400_BAD_REQUEST)

#Actualizar  
@api_view(['GET','PUT'])
def PostApiViewSet_Post(request, pk=None):
    
    if request.method == 'GET':
        consulta = Empresa.objects.raw("")  
        serializer_empresas = PostSerializer(consulta, many = True)
        return Response(serializer_empresas.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        #Buscar entre una lista al elemento o recibir el elemento a actualizar
        consulta = Empresa.objects.filter(id = pk).first()  
        #Pasamos el objeto al serializador y lo actualiza con la data enviada
        #return response({message:'Mensaje Cualquiera'})
        serializer_empresas = PostSerializer(consulta, data = request.data)
        if serializer_empresas.is_valid():
            serializer_empresas.save()
            return response(serializer_empresas.data, status = status.HTTP_200_OK)
        return response(serializer_empresas.errors, status = status.HTTP_400_BAD_REQUEST)

    

