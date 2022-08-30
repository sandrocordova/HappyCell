from ast import Break, Delete, Index, Or, Return
from asyncio.windows_events import NULL
import json
from os import remove
from queue import Empty
from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework import status
from apps.apihc.functions import actualizarDireccion, actualizarTelefono, guardarDireccion, guardarTelefono, validarDireccion, validarTelefono
from apps.apihc.models import Cliente, Direccion, Telefono # Manejo de Status
from apps.apihc.serializers import DireccionSerializer, TelefonoSerializer

class direccionSearch(APIView):
    def post(self, request):
        clienteId = request.data['clie_codigo']
        direccionRetornada = Direccion.objects.using('clientes').filter(CLIE_CODIGO=clienteId).all()
        direcciones = []
        if direccionRetornada:
            for direccion in direccionRetornada:
                if not direcciones or not list_contains(direcciones,direccion.TIDE_CODIGO):
                    direcciones.append(direccion)
            serializer_cliente = DireccionSerializer(direcciones, many=True)
            return Response(serializer_cliente.data)
        return Response("El cliente no tiene direcciones registradas", status=status.HTTP_400_BAD_REQUEST)

def list_contains(arreglo,objeto):
    for item in arreglo:        
        if item.TIDE_CODIGO == objeto:
            return True
    return False
        
class telefonoSearch(APIView):
    def post(self, request):
        clienteId = request.data['clie_codigo']
        direccionId = request.data['dire_codigo']
        telefonoRetornado = Telefono.objects.using('clientes').filter(
            DIRE_CODIGO=direccionId, CLIE_CODIGO=clienteId).all()
        if telefonoRetornado:
            serializer_cliente = TelefonoSerializer(telefonoRetornado, many=True)
            return Response(serializer_cliente.data, status=status.HTTP_200_OK)
        return Response("La dirección del cliente no tiene un teléfono relacionado", status=status.HTTP_400_BAD_REQUEST)
    
class DireccionView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        direcciones = data['direcciones']
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
            
        for direccion in direcciones:
            dire_descripcion = direccion["DIRE_DESCRIPCION"]

            direccionExistente = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, DIRE_DESCRIPCION = dire_descripcion).first()
            if direccionExistente is None:
                direccion['DIRE_CODIGO'] = 1
                dire_codigo = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-DIRE_CODIGO').first()
                if dire_codigo:
                    direccion['DIRE_CODIGO'] = dire_codigo.DIRE_CODIGO + 1
                direccion['CIUD_CODIGO'] = 223
                direccion['CLIE_CODIGO'] = clie_codigo
                validarD = validarDireccion(direccion)
                if validarD['status'] is False:
                    return Response({"status": 400, "message": validarD['message']}, status = status.HTTP_400_BAD_REQUEST)
                guardarD = guardarDireccion(direccion)
                # Validar que el número enviado no esté registrado para el Cliente
            else:
                return Response({"status": 400, "message": f"La dirección {dire_descripcion} ya existe"}, status = status.HTTP_400_BAD_REQUEST)
        
        return Response({"status": 200, "message": f"Se agregaron las direcciones al cliente {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        direcciones = data['direcciones']
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        success = 0

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
        
        for direccion in direcciones:
            direccion['CLIE_CODIGO'] = clie_codigo
            direccionChecking = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, DIRE_CODIGO = direccion['DIRE_CODIGO']).first()
            if direccionChecking is None:
                return Response({"status": 400, "message": f"Dirección no existe con el DIRE_CODIGO: {direccion['DIRE_CODIGO']} para el Cliente {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
            validarD = validarDireccion(direccion)
            if validarD['status'] is False:
                return Response({"status": 400, "message": validarD['message']}, status = status.HTTP_400_BAD_REQUEST)
            actualizarD = actualizarDireccion(direccion, direccionChecking)
            if actualizarD > 0:
                success += 1

        return Response({"status": 200, "message": f"Se actualizaron {success} de {len(direcciones)} Direcciones del Cliente {clie_codigo}"}, status = status.HTTP_200_OK)

class TelefonoView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        telefonos = data['telefonos']
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
        
        for telefono in telefonos:
            tele_numero = telefono['TELE_NUMERO']
            telefonoExistente = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TELE_NUMERO = tele_numero).first()
            if telefonoExistente is None:
                telefono['TELE_CODIGO'] = 1
                telefono['CLIE_CODIGO'] = clie_codigo
                tele_codigo = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-TELE_CODIGO').first()
                if tele_codigo:
                    telefono['TELE_CODIGO'] = tele_codigo.TELE_CODIGO + 1
                validarT = validarTelefono(telefono)
                if validarT['status'] is False:
                    return Response({"status": 400, "message": validarT['message']}, status = status.HTTP_400_BAD_REQUEST)
                guardarT = guardarTelefono(telefono)
            else:
                return Response({"status": 409, "message": f"El teléfono {tele_numero} ya existe"}, status = status.HTTP_409_CONFLICT)

        return Response({"status": 200, "message": f"Se agregaron los teléfonos al cliente {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        telefonos = data['telefonos']
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        success = 0

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
        
        for telefono in telefonos:
            telefono['CLIE_CODIGO'] = clie_codigo
            telefonoChecking = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, DIRE_CODIGO = telefono['DIRE_CODIGO'], TELE_CODIGO = telefono['TELE_CODIGO']).first()
            if telefonoChecking is None:
                return Response({"status": 400, "message": f"Teléfono no existe con el TELE_CODIGO: {telefono['TELE_CODIGO']} y DIRE_CODIGO: {telefono['DIRE_CODIGO']} para el Cliente {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
            validarT = validarTelefono(telefono)
            if validarT['status'] is False:
                return Response({"status": 400, "message": validarT['message']}, status = status.HTTP_400_BAD_REQUEST)
            actualizarT = actualizarTelefono(telefono, telefonoChecking)
            if actualizarT > 0:
                success += 1

        return Response({"status": 200, "message": f"Se actualizaron {success} de {len(telefonos)} Teléfonos del Cliente {clie_codigo}"}, status = status.HTTP_200_OK)