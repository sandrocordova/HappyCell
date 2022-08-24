from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.cliente.models import Cliente
from apps.apihc.models import Direccion, Telefono
from apps.apihc.serializers import DireccionSerializer, TelefonoSerializer
from apps.cliente.serializer import ClienteSerializer

class direccion_search(APIView):
    def post(self, request): # 
        # Inicio Reservar información a manejar a partir del Request
        clienteId = request.data['clie_codigo']
        clienteChecking = Direccion.objects.using('clientes').filter(CLIE_CODIGO = clienteId).all()
        if clienteChecking:
            serializer_cliente = DireccionSerializer(clienteChecking, many=True)
            return Response(serializer_cliente.data, status = status.HTTP_200_OK)
        return Response("Dirección de cliente no encontrado", status = status.HTTP_400_BAD_REQUEST)
    
class telefono_search(APIView):
    def post(self, request): # 
        # Inicio Reservar información a manejar a partir del Request
        clienteId = request.data['clie_codigo']
        clienteId = request.data['dir']
        clienteChecking = Telefono.objects.using('clientes').filter(CLIE_CODIGO = clienteId).all()
        if clienteChecking:
            serializer_cliente = TelefonoSerializer(clienteChecking, many=True)
            return Response(serializer_cliente.data, status = status.HTTP_200_OK)
        return Response("Dirección de cliente no encontrado", status = status.HTTP_400_BAD_REQUEST)
        
class cliente_search(APIView):
    def get(self, request):
        clientes = Cliente.objects.using('clientes').all()[4378:4450]
        for cliente in clientes:
            if cliente.TICL_CODIGO == "N":
                cliente.TICL_CODIGO = "Natural"
            else:
                cliente.TICL_CODIGO = "Juridico"
        
        serializer_cliente = ClienteSerializer(clientes, many = True)
        return Response(serializer_cliente.data, status = status.HTTP_200_OK)
    
    def post(self, request): # 
        # Inicio Reservar información a manejar a partir del Request
        clienteData = request.data['data']
        if cedula_is_ok(clienteData):
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = clienteData).first()
            serializer_cliente = ClienteSerializer(clienteChecking)
            return Response(serializer_cliente.data, status = status.HTTP_200_OK)
        else :     
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_NOMBRE__icontains = clienteData).all()
            if clienteChecking:
                serializer_cliente = ClienteSerializer(clienteChecking, many=True)
                return Response(serializer_cliente.data, status = status.HTTP_200_OK)
            return Response("Cliente no encontrado", status = status.HTTP_400_BAD_REQUEST)
        
def cedula_is_ok(cedula):
    if cedula.isdigit():
        if len(cedula)>=10:
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
    
    