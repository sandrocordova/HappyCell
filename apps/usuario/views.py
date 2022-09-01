from rest_framework.views import APIView # Procesamiento de Views
from rest_framework.response import Response # Manejo de Response HTTP
from rest_framework.exceptions import AuthenticationFailed # Validación de Token (sin expirar)
from rest_framework import status # Manejo de Status
import jwt, datetime, base64
from apps.apihc.serializers import UsuarioSerializer
from apps.apihc.models import Usuario
from django.shortcuts import render

# Create your views here.

# Create your views here.
class getToken(APIView):
    def post(self, request):
        headers = request.headers
        if 'User' not in headers:
            raise AuthenticationFailed('¡Envía un Usuario!')
            
        basicTokenEncrypt = headers['User']
        passwordEncrypt = headers['Password']
        usua_login = base64.b64decode(basicTokenEncrypt)
        usua_login = usua_login.decode()
        password_login = base64.b64decode(passwordEncrypt)
        password_login = password_login.decode()

        usuario = Usuario.objects.filter(USUA_LOGIN=usua_login).first()

        if usuario is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        if not usuario.USUA_CLAVE.__eq__(password_login):
            raise AuthenticationFailed('Contraseña incorrecta')
        
        payload = {
            'id': usuario.USUA_LOGIN,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'tfhc-pc-pydj-bkd-mssql', algorithm = 'HS256')

        response = Response()

        response.data = {
            'jwt': token
            #'User': usua_login
        }

        return response

class validate(APIView):
    def post(self, request):
        headers = request.headers
        if 'Bearer' not in headers:
            raise AuthenticationFailed('Envía un token!')

        token = headers['Bearer']

        if not token:
            raise AuthenticationFailed('Envía un token!')

        try:
            payload = jwt.decode(token, 'tfhc-pc-pydj-bkd-mssql', algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expiró!')

        usuario = Usuario.objects.filter(USUA_LOGIN=payload['id']).first()
        if usuario is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        usuarioSerializer = UsuarioSerializer(usuario)

        userDict = usuarioSerializer.data

        del userDict['USUA_CLAVE']
        return Response(userDict)

def authenticate(request):
    headers = request.headers
    if 'Bearer' not in headers:
        return {"status": status.HTTP_401_UNAUTHORIZED, "message": "Envía un token!"}

    token = headers['Bearer']

    if not token:
        return {"status": status.HTTP_401_UNAUTHORIZED, "message": "Envía un token!"}
    try:
        payload = jwt.decode(token, 'tfhc-pc-pydj-bkd-mssql', algorithms = ['HS256'])
    except jwt.ExpiredSignatureError:
        return {"status": status.HTTP_401_UNAUTHORIZED, "message": "Token expiró!"}

    usuario = Usuario.objects.filter(USUA_LOGIN=payload['id']).first()
    
    if usuario is None:
        return {"status": status.HTTP_204_NO_CONTENT, "message": "No se encontró usuario!"}
    
    usuarioSerializer = UsuarioSerializer(usuario)

    userDict = usuarioSerializer.data

    del userDict['USUA_CLAVE']
    return {"status": status.HTTP_200_OK, "message": "Autenticación exitosa!", "Usuario": userDict}
