from django.contrib import admin
from django.urls import path, include
from apps.agencia.views import menu


urlpatterns = [
    path('', menu, name = 'menu'),
    path('api/', include('apps.cliente.api.urls')),
]
