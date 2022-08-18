from django.urls import path
from apps.cliente.views import cliente_api_view


urlpatterns = [
    path('view', cliente_api_view, name='api_cliente'),
]
