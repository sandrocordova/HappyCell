from rest_framework import serializers
from apps.cliente.models import Cliente
from apps.apihc.models import Direccion, Telefono

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
