from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework import status # Manejo de Status
from apps.apihc.functions import guardarObservacion, validarObservacion
from apps.apihc.models import Observacion

class ObservacionClienteView(APIView):
    def post(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        observaciones = data['observaciones']
        for observacion in observaciones:
            tioc_codigo = observacion['TIOC_CODIGO']
            observacion['CLIE_CODIGO'] = clie_codigo
            validarO = validarObservacion(observacion)
            if validarO['status'] is False:
                return Response({"status": 400, "message": validarO['message']}, status = status.HTTP_400_BAD_REQUEST)
            # Inicio Validar-Observaciones
            observacionExiste = Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TIOC_CODIGO = tioc_codigo).first()
            if observacionExiste is None:
                observacion['OBCL_CODIGO'] = 1
                obcl_codigo = Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo).order_by('-OBCL_CODIGO').first()
                if obcl_codigo:
                    observacion['OBCL_CODIGO'] = obcl_codigo.OBCL_CODIGO + 1
                guardarObservacion(observacion)
            else:
                return Response({"status": 409, "message": f"La obserbación de tipo {tioc_codigo} ya existe"}, status = status.HTTP_409_CONFLICT)

        return Response({"status": 200, "message": f"Se agregaron las observaciones al cliente {clie_codigo}"}, status = status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        clie_codigo = data['CLIE_CODIGO']
        observaciones = data['observaciones']
        for observacion in observaciones:
            tioc_codigo = observacion['TIOC_CODIGO']
            validarO = validarObservacion(observacion)
            if validarO['status'] is False:
                return Response({"status": 400, "message": validarO['message']}, status = status.HTTP_400_BAD_REQUEST)
            # Inicio Validar-Observaciones
            observacionExiste = Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TIOC_CODIGO = tioc_codigo).first()
            if observacionExiste:
                Observacion.objects.using('clientes').filter(CLIE_CODIGO = clie_codigo, TIOC_CODIGO = tioc_codigo).update(OBCL_DESCRI = observacion['OBCL_DESCRI'])
            else:
                return Response({"status": 400, "message": f"La obserbación de tipo {tioc_codigo} no existe"}, status = status.HTTP_400_BAD_REQUEST)

        return Response({"status": 200, "message": f"Se actualizaron las observaciones al cliente {clie_codigo}"}, status = status.HTTP_200_OK)