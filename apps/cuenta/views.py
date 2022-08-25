from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework import status
from apps.apihc.functions import guardarCuentaBancaria, validarCuenta

from apps.apihc.models import CuentaBancariaCliente

class CuentaBancariaView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        cuentas = data['cuentas']
                
        for cuenta in cuentas:
            cubc_cuenta = cuenta['CUBC_CUENTA']
            cuenta['CLIE_CODIGO'] = clie_codigo
            cuentaExiste = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, CUBC_CUENTA = cubc_cuenta).first()
            if cuentaExiste is None:                    
                cuenta['CUBC_CODIGO'] = 1
                cubc_codigo = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-CUBC_CODIGO').first()
                if cubc_codigo:
                    cuenta['CUBC_CODIGO'] = cubc_codigo.CUBC_CODIGO + 1
                
                validarCB = validarCuenta(cuenta)
                if validarCB['status'] is False:
                    return Response({"status": 400, "message": validarCB['message']}, status = status.HTTP_400_BAD_REQUEST)
                guardarCB = guardarCuentaBancaria(cuenta)
            else:
                return Response({"status": 400, "message": f"La cuenta {cubc_cuenta} ya existe"}, status = status.HTTP_400_BAD_REQUEST)
            
        return Response({"status": 200, "message": f"Se agregaron las referencia bancarias del cliente {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        cuentas = data['cuentas']