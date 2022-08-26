import datetime
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.apihc.functions import actualizarCliente, actualizarClienteJuridico, actualizarClienteNatural, guardarAsesorCliente, guardarCliente, guardarClienteJuridico, guardarClienteNatural, validarCliente, validarClienteAsesor, validarClienteJuridico, validarClienteNatural
from apps.apihc.models import ClienteAsesor, ClienteJuridico, ClienteNatural, Secuencia
from apps.apihc.serializers import ClienteNaturalSerializer, ClienteJuridicoSerializer
from apps.cliente.models import Cliente
from apps.catalog.models import TipoDocumento
from apps.catalog.serializer import TipoDocumentoSerializer
from apps.cliente.serializer import ClienteSerializer
from django.core.paginator import Paginator

class cliente_search(APIView):
    def get(self, request):
        clientes = Cliente.objects.using('clientes').all()[:1]
        
        consulta = TipoDocumento.objects.using('clientes').all()
        profesionesSerializer = TipoDocumentoSerializer(consulta, many = True)
        
        print(consulta[:])
        print(consulta[0])
        print(consulta[1])
        print(consulta[2])
        print(profesionesSerializer.data[2]["TIDO_CODIGO"])
        print("----------------------")
        print()
            
        for cliente in clientes:
            catalog_list =[]
            json_response = {
            'codigo': "N",
            'significado': "Natural"
            }
            
            
            if cliente.TICL_CODIGO == "N":
                catalog_list.append(cliente.TICL_CODIGO)
                catalog_list.append("Natural")
                #cliente.TICL_CODIGO = json_response
            else:
                cliente.TICL_CODIGO = "Juridico"

        serializer_cliente = ClienteSerializer(clientes, many=True)
        return Response(serializer_cliente.data, status=status.HTTP_200_OK)

    def post(self, request):
        clienteData = request.data['data']
        if cedula_is_ok(clienteData):
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION__contains=clienteData).first()
            if serializer_cliente:
                paginador = Paginator(clienteChecking, 1)
                pagina = request.GET.get("page") or 1
                clienteChecking = paginador.get_page(pagina)
                pagina_actual = int(pagina)                
                serializer_cliente = ClienteSerializer(clienteChecking, many=True)
                json_response = {
                    'status': True,
                    'message': "Response exitoso",
                    "pagina_actual": pagina_actual,
                    "paginas": clienteChecking.paginator.num_pages,
                    "cliente": serializer_cliente.data
                }
                return Response(serializer_cliente.data, status=status.HTTP_200_OK)
            return Response("No se encontró un cliente con dicha Cédula, RUC o Pasaporte", status=status.HTTP_404_NOT_FOUND)
        
        
        elif str_is_ok(clienteData):  
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_NOMBRE__icontains=clienteData).all()
            if clienteChecking:
                paginador = Paginator(clienteChecking, 1)
                pagina = request.GET.get("page") or 1
                clienteChecking = paginador.get_page(pagina)
                pagina_actual = int(pagina)                
                serializer_cliente = ClienteSerializer(clienteChecking, many=True)
                json_response = {
                    'status': True,
                    'message': "Response exitoso",
                    "pagina_actual": pagina_actual,
                    "paginas": clienteChecking.paginator.num_pages,
                    "cliente": serializer_cliente.data
                }
                return Response(json_response, status=status.HTTP_200_OK)
            return Response("No se encontró un cliente con nombre: "+clienteData, status=status.HTTP_404_NOT_FOUND)              
        return Response("Información insuficiente para buscar un cliente", status=status.HTTP_400_BAD_REQUEST)


def cedula_is_ok(cedula):
    if cedula.isdigit():
        if len(cedula) >= 5:
            return True
        return False
    return False

def str_is_ok(cedula):
    if len(cedula) >= 3:
        return True
    return False    

@api_view(['GET'])
def cliente_api_view(request):

    if request.method == 'GET':
        clientes = Cliente.objects.using('clientes').all()[4378:4450]
        for cliente in clientes:
            if cliente.TICL_CODIGO == "N":
                cliente.TICL_CODIGO = "Natural"
            else:
                cliente.TICL_CODIGO = "Juridico"
        
        serializer_cliente = ClienteSerializer(clientes, many = True)
        return Response(serializer_cliente.data, status = status.HTTP_200_OK)
    
class ClienteView(APIView):
    def post(self, request):
        data = request.data
        informacionCliente = data['cliente']
        detalleCliente = data['detalle']

        secuencia = Secuencia.objects.using('clientes').filter(SECU_TABLA = 'CLIENTE', EMPR_CODIGO = '8').first()
        clie_codigo = secuencia.SECU_VALOR_ACTUAL
        ticl_codigo = informacionCliente['TICL_CODIGO']
        clie_identificacion = informacionCliente['CLIE_IDENTIFICACION']
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = clie_identificacion).first()
        today = datetime.datetime.now()
        clie_fecha_creacion = today.strftime("%Y-%m-%d %H:%M:%S")
        informacionCliente['CLIE_FECHA_CREACION'] = clie_fecha_creacion
        informacionCliente['CLIE_CODIGO'] = clie_codigo
        detalleCliente['CLIE_CODIGO'] = clie_codigo

        if clienteChecking:
            return Response({"status": 409, "message": f"CLIENTE ya existe con la CLAVE IDENTIFICACIÓN: {clie_identificacion}"}, status = status.HTTP_409_CONFLICT)
        if cedula_is_ok(clie_identificacion) is False:
            return Response({"status": 400, "message": f"CLAVE IDENTIFICACIÓN: {clie_identificacion} INCORRECTA"}, status = status.HTTP_400_BAD_REQUEST)

        validarC = validarCliente(informacionCliente)
        if validarC['status'] is False:
            return Response({"status": 400, "message": validarC['message']}, status = status.HTTP_400_BAD_REQUEST)

        if ticl_codigo == 'N':
            validarCN = validarClienteNatural(detalleCliente)
            if validarCN['status'] is False:
                return Response({"status": 400, "message": validarCN['message']}, status = status.HTTP_400_BAD_REQUEST)
            guardarClienteNatural(detalleCliente)
        if ticl_codigo == 'J':
            validarCJ = validarClienteJuridico(detalleCliente)
            if validarCJ['status'] is False:
                return Response({"status": 400, "message": validarCJ['message']}, status = status.HTTP_400_BAD_REQUEST)
            guardarClienteJuridico(detalleCliente)

        guardarCliente(informacionCliente)

        secuencia = Secuencia.objects.using('clientes').filter(SECU_TABLA = 'CLIENTE', EMPR_CODIGO = '8').update(SECU_VALOR_ACTUAL = clie_codigo + 1)

        return Response({"status": 200, "message": f"Se agregó al cliente {ticl_codigo} {clie_identificacion} con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        informacionCliente = data['cliente']
        detalleSCliente = data['detalle']

        clie_codigo = informacionCliente['CLIE_CODIGO']
        ticl_codigo = informacionCliente['TICL_CODIGO']
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)

        validarC = validarCliente(informacionCliente)
        if validarC['status'] is False:
            return Response({"status": 400, "message": validarC['message']}, status = status.HTTP_400_BAD_REQUEST)
        if ticl_codigo == 'N':
            detalleCliente = ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
            validarCN = validarClienteNatural(detalleSCliente)
            if validarCN['status'] is False:
                return Response({"status": 400, "message": validarCN['message']}, status = status.HTTP_400_BAD_REQUEST)
            cambiosCD = actualizarClienteNatural(detalleSCliente, detalleCliente)
            tipo = 'Natural'
        if ticl_codigo == 'J':
            detalleCliente = ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
            validarCJ = validarClienteJuridico(detalleSCliente)
            if validarCJ['status'] is False:
                return Response({"status": 400, "message": validarCJ['message']}, status = status.HTTP_400_BAD_REQUEST)
            cambiosCD = actualizarClienteJuridico(detalleSCliente, detalleCliente)
            tipo = 'Jurídico'
        cambiosC = actualizarCliente(informacionCliente, clienteChecking)

        return Response({"status": 200, "message": f"Se actualizaron {cambiosC} datos de Cliente {clie_codigo} y {cambiosCD} datos de Cliente {tipo}"}, status = status.HTTP_200_OK)

    def get(self, request):
        data = request.GET
        clie_codigo = data['codigo']

        cliente = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if cliente is None:
            return Response({"status": 204, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_204_NO_CONTENT)
        
        clienteSerializado = ClienteSerializer(cliente)
        ticl_codigo = cliente.TICL_CODIGO
        if ticl_codigo == 'N':
            detalle = ClienteNatural.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
            detalleSerializado = ClienteNaturalSerializer(detalle)

        if ticl_codigo == 'J':
            detalle = ClienteJuridico.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
            detalleSerializado = ClienteJuridicoSerializer(detalle)

        return Response({"status": 200, "data": {'cliente': clienteSerializado.data, 'detalle': detalleSerializado.data}}, status = status.HTTP_200_OK)

class ClienteAsesorView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        asesor = data['asesor']
        ases_codigo = asesor['ASES_CODIGO']

        cliente = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if cliente is None:
            return Response({"status": 204, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_204_NO_CONTENT)
        
        asesorClienteExiste = ClienteAsesor.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        if asesorClienteExiste is None:
            validarCA = validarClienteAsesor(ases_codigo)
            if validarCA['status'] is False:
                return Response({"status": 400, "message": validarCA['message']}, status = status.HTTP_400_BAD_REQUEST)
            asesor['CLIE_CODIGO'] = clie_codigo
            asesor['EMPR_CODIGO'] = 8
            guardarAsesorCliente(asesor)
        else:
            return Response({"status": 409, "message": f"El cliente {clie_codigo} ya tiene un asesor registrado"}, status = status.HTTP_409_CONFLICT)

        return Response({"status": 200, "message": f"Se agrego el asesor {ases_codigo} al cliente {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        asesor = data['asesor']
        
        cliente = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if cliente is None:
            return Response({"status": 204, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_204_NO_CONTENT)
        
        asesorClienteExiste = ClienteAsesor.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        if asesorClienteExiste != None:
            validarCA = validarClienteAsesor(asesor)
            if validarCA['status'] is False:
                return Response({"status": 400, "message": validarCA['message']}, status = status.HTTP_400_BAD_REQUEST)
            ClienteAsesor.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).update(ASES_CODIGO = asesor)
        else:
            return Response({"status": 409, "message": f"El cliente {clie_codigo} no tiene un asesor registrado"}, status = status.HTTP_409_CONFLICT)

        return Response({"status": 200, "message": f"Se actualizó el asesor {asesor} al cliente {clie_codigo}"}, status = status.HTTP_200_OK)