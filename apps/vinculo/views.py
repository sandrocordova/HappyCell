from ast import Index
from asyncio.windows_events import NULL
import datetime
from multiprocessing.sharedctypes import Value
from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework import status # Manejo de Status
from apps.apihc.functions import actualizarVinculo, guardarVinculo, validarVinculo
from apps.apihc.models import Cliente, Vinculo
from apps.apihc.serializers import VinculoSerializer

class VinculoView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        ticl_codigo = data['TICL_CODIGO']
        vinculos = data['vinculos']
        today = datetime.datetime.now()
        vin_fecha_creacion = today.strftime("%Y-%m-%d %H:%M:%S")

        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
        
        for vinculo in vinculos:
            vinc_identificacion = vinculo["VINC_IDENTIFICACION"]
            vinculo['VIN_FECHA_INGRESA'] = vin_fecha_creacion
            # Validar que el vínculo enviado no esté registrado para el Cliente
            vinculoExistente = Vinculo.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, VINC_IDENTIFICACION = vinc_identificacion).first()
            if vinculoExistente is None:
                vinculo['VINC_CODIGO'] = 1
                vinculo['TICL_CODIGO'] = ticl_codigo
                vinc_codigo = Vinculo.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-VINC_CODIGO').first()
                if vinc_codigo:
                    vinculo['VINC_CODIGO'] = vinc_codigo.VINC_CODIGO + 1
                vinculo['CLIE_CODIGO'] = clie_codigo
                vinculo['VIN_ESTADO'] = "A"
                # vinculo['CIUD_CODIGO'] = 223

                varlidarV = validarVinculo(vinculo)
                if varlidarV['status'] is False:
                    return Response({"status": 400, "message": varlidarV['message']}, status = status.HTTP_400_BAD_REQUEST)

                guardarVinculo(vinculo)
            else:
                return Response({"status": 409, "message": f"Algunos de los vínculos del cliente {clie_codigo} ya existe"}, status = status.HTTP_409_CONFLICT)

        return Response({"status": 200, "message": f"Se agregaron los vínculos al cliente {clie_codigo}"}, status = status.HTTP_200_OK)


        #Fin Validar-Cliente

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        vinculos = data['vinculos']      
        ticl_codigo = data['TICL_CODIGO']  
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()
        success = 0

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
        
        for vinculo in vinculos:
            vinculo['CLIE_CODIGO'] = clie_codigo
            vinculo['TICL_CODIGO'] = ticl_codigo
            vinculoChecking = Vinculo.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, VINC_CODIGO = vinculo['VINC_CODIGO']).first()
            if vinculoChecking is None:
                return Response({"status": 400, "message": f"Vinculo no existe con el VINC_CODIGO: {vinculo['VINC_CODIGO']} para el Cliente {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
            validarV = validarVinculo(vinculo)
            if validarV['status'] is False:
                return Response({"status": 400, "message": validarV['message']}, status = status.HTTP_400_BAD_REQUEST)
            actualizarV = actualizarVinculo(vinculo, vinculoChecking)
            if actualizarV > 0:
                success += 1

        return Response({"status": 200, "message": f"Se actualizaron {success} de {len(vinculos)} Vínculos del Cliente {clie_codigo}"}, status = status.HTTP_200_OK)


class vinculoSearch(APIView):
    def post(self, request):
        clienteId = request.data['clie_codigo']
        vinculosRetornados = Vinculo.objects.using('clientes').filter(CLIE_CODIGO=clienteId).all()
        vinculos = []
        if vinculosRetornados:
            for vinculo in vinculosRetornados:
                if not vinculos:
                    vinculos.append(vinculo)
                    print("AGREGO ")
                else:
                #elif (list_contains(vinculos,vinculo.VINC_CODIGO, vinculo.TIVI_CODIGO)):
                    flag = True
                    for item in vinculos:
                        if int(item.TIVI_CODIGO) == int(vinculo.TIVI_CODIGO):
                            flag = False
                            if int(vinculo.VINC_CODIGO) >= int(item.VINC_CODIGO):
                                vinculos.remove(item)
                                vinculos.append(vinculo)
                                break
                    if flag: vinculos.append(vinculo)
                    
                    
            serializer_cliente = VinculoSerializer(vinculos, many=True)
            return Response(serializer_cliente.data)
        return Response("El cliente no tiene vinculos registrados", status=status.HTTP_400_BAD_REQUEST)

def list_contains(arreglo,clienteCod, vinculoCod):
    flag = False
    for item in arreglo:
        if int(item.TIVI_CODIGO) == int(vinculoCod):
            if int(clienteCod) >= int(item.VINC_CODIGO):
                return True
            else: flag = True
    if flag: return False
    else: return True
