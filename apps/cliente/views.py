import datetime
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.apihc.functions import actualizarCliente, actualizarClienteJuridico, actualizarClienteNatural, guardarCliente, guardarClienteJuridico, guardarClienteNatural, validarCliente, validarClienteJuridico, validarClienteNatural
from apps.apihc.models import ClienteJuridico, ClienteNatural, Secuencia, Direccion
from apps.cliente.models import Cliente
from apps.apihc.models import Direccion, Telefono
from apps.apihc.serializers import DireccionSerializer, TelefonoSerializer, ClienteNaturalSerializer, ClienteJuridicoSerializer

from apps.cliente.serializer import ClienteSerializer
from django.core.paginator import Paginator

class direccion_search(APIView):
    def post(self, request):
        clienteId = request.data['clie_codigo']
        direccionRetornada = Direccion.objects.using(
            'clientes').filter(CLIE_CODIGO=clienteId).all()
        if direccionRetornada:
            serializer_cliente = DireccionSerializer(direccionRetornada, many=True)
            return Response(serializer_cliente.data, status=status.HTTP_200_OK)
        return Response("El cliente no tiene direcciones registradas", status=status.HTTP_400_BAD_REQUEST)


class telefono_search(APIView):
    def post(self, request):
        clienteId = request.data['clie_codigo']
        direccionId = request.data['dire_codigo']
        telefonoRetornado = Telefono.objects.using('clientes').filter(
            DIRE_CODIGO=direccionId, CLIE_CODIGO=clienteId).all()
        if telefonoRetornado:
            serializer_cliente = TelefonoSerializer(telefonoRetornado, many=True)
            return Response(serializer_cliente.data, status=status.HTTP_200_OK)
        return Response("La dirección del cliente no tiene un teléfono relacionado", status=status.HTTP_400_BAD_REQUEST)


class cliente_search(APIView):
    def get(self, request):
        clientes = Cliente.objects.using('clientes').all()[4378:4450]
        
        for cliente in clientes:
            catalog_list =[]
            json_response = {
            'codigo': "N",
            'significado': "Natural"
            }
            if cliente.TICL_CODIGO == "N":
                
                catalog_list.append(cliente.TICL_CODIGO)
                catalog_list.append("Natural")
                cliente.TICL_CODIGO = json_response
            else:
                cliente.TICL_CODIGO = "Juridico"

        serializer_cliente = ClienteSerializer(clientes, many=True)
        return Response(serializer_cliente.data, status=status.HTTP_200_OK)

    def post(self, request):
        clienteData = request.data['data']
        if cedula_is_ok(clienteData):
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION=clienteData).first()
            serializer_cliente = ClienteSerializer(clienteChecking)
            return Response(serializer_cliente.data, status=status.HTTP_200_OK)
        else:
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_NOMBRE__icontains=clienteData).all()
            if clienteChecking:
                for cliente in clienteChecking:
                    catalog_list =[]
                    if cliente.TICL_CODIGO == "N":
                        catalog_list.append(cliente.TICL_CODIGO)
                        catalog_list.append("Natural")
                        cliente.TICL_CODIGO = catalog_list
                    else:
                        cliente.TICL_CODIGO = "Juridico"
                    if cliente.TIDO_CODIGO == "C":
                        cliente.TIDO_CODIGO = "Cédula"
                    elif cliente.TIDO_CODIGO == "P":
                        cliente.TIDO_CODIGO = "Pasaporte"
                    elif cliente.TIDO_CODIGO == "R":
                        cliente.TIDO_CODIGO = "Ruc"
                         
                paginador = Paginator(clienteChecking, 1)
                pagina = request.GET.get("page") or 1
                clienteChecking = paginador.get_page(pagina)
                pagina_actual = int(pagina)
                pagina_total = list(range(1, clienteChecking.paginator.num_pages+1))
                
                serializer_cliente = ClienteSerializer(clienteChecking, many=True)
                json_response = {
                    'status': True,
                    'message': "Response exitoso",
                    "pagina_actual": pagina_actual,
                    "paginas": pagina_total,
                    "cliente": serializer_cliente.data
                }
                return Response(json_response, status=status.HTTP_200_OK)
            else:
                clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION__contains=clienteData).all()
                if clienteChecking:
                    serializer_cliente = ClienteSerializer(clienteChecking, many=True)
                    return Response(serializer_cliente.data, status=status.HTTP_200_OK)
                
            return Response("Cliente no encontrado", status=status.HTTP_400_BAD_REQUEST)


def cedula_is_ok(cedula):
    if cedula.isdigit():
        if len(cedula) >= 10:
            return True
        return False
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
