from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.cliente.models import Cliente
from apps.cliente.serializer import ClienteSerializer

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
        print("MENSAJE RECIBIDO ------------------------"+request.data)
        if cedula_is_ok(clienteData):
            print("Es cédula")
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_IDENTIFICACION = clienteData).first()
            print(clienteChecking)
            serializer_cliente = ClienteSerializer(clienteChecking)
            return Response(serializer_cliente.data, status = status.HTTP_200_OK)
        else :     
            print("NO ES CEDULA")
            clienteChecking = Cliente.objects.using('clientes').filter(CLIE_NOMBRE = clienteData).first()
            print(clienteChecking)
            print("NO ES CEDULA")
            if clienteChecking:
                print(clienteChecking)
                print("Elementos encontrados: "+len(clienteChecking))
                serializer_cliente = ClienteSerializer(clienteChecking)
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
    
    