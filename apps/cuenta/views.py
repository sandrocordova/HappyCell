from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework import status
from apps.apihc.functions import actualizarCuenta, guardarCuentaBancaria, validarCuenta

from apps.apihc.models import Cliente, CuentaBancariaCliente

class CuentaBancariaView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        cuentas = data['cuentas']
        
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
          
                
        for cuenta in cuentas:
            cubc_cuenta = cuenta['CUBC_CUENTA']
            ticu_codigo = cuenta['TICU_CODIGO']
            cuenta['CLIE_CODIGO'] = clie_codigo
            cuentaExiste = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, CUBC_CUENTA = cubc_cuenta).first()
            tipoCuentaExiste = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TICU_CODIGO = ticu_codigo).first()
            if cuentaExiste is None and tipoCuentaExiste is None:                    
                cuenta['CUBC_CODIGO'] = 1
                cubc_codigo = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-CUBC_CODIGO').first()
                if cubc_codigo:
                    cuenta['CUBC_CODIGO'] = cubc_codigo.CUBC_CODIGO + 1
                validarCB = validarCuenta(cuenta)
                if validarCB['status'] is False:
                    return Response({"status": 400, "message": validarCB['message']}, status = status.HTTP_400_BAD_REQUEST)
                guardarCB = guardarCuentaBancaria(cuenta)
            else:
                return Response({"status": 400, "message": f"La cuenta {cubc_cuenta} o tipo de cuenta {ticu_codigo} ya existe para el cliente {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
            
        return Response({"status": 200, "message": f"Se agregaron las referencia bancarias del cliente {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        cuentas = data['cuentas']
        
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
          
        for cuenta in cuentas:
            cubc_codigo = cuenta['CUBC_CODIGO']
            cuenta['CLIE_CODIGO'] = clie_codigo
            cuentaExiste = CuentaBancariaCliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, CUBC_CODIGO = cubc_codigo).first()
            if cuentaExiste :    
                validarCB = validarCuenta(cuenta)
                if validarCB['status'] is False:
                    return Response({"status": 400, "message": validarCB['message']}, status = status.HTTP_400_BAD_REQUEST)
                actualizarCuenta(cuenta, cuentaExiste)
            else:
                return Response({"status": 400, "message": f"La cuenta {cubc_codigo} no existe para el cliente {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
       
        return Response({"status": 200, "message": f"Se actualizaron las cuentas al cliente {clie_codigo}"}, status = status.HTTP_200_OK)

class BalanceCuenta(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        balances = data['cuentas']
        
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
          

        return Response({}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        balances = data['cuentas']
        
        clienteChecking = Cliente.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).first()

        if clienteChecking is None:
            return Response({"status": 400, "message": f"Cliente no existe con el CLIE_CODIGO: {clie_codigo}"}, status = status.HTTP_400_BAD_REQUEST)
          

        return Response({}, status = status.HTTP_200_OK)
