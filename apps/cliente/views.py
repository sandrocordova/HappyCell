from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from apps.cliente.models import Cliente
from apps.cliente.serializer import ClienteSerializer

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