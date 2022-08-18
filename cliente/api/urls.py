from django.urls import path
from apps.agencia.api.views import cliente_api_view


urlpatterns = [
    path('cliente', cliente_api_view, name='api_cliente'),
]
