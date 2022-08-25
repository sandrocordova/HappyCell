from django.contrib import admin
from django.urls import path, include
from HappyCell.view import menu

urlpatterns = [
    path('', menu, name="menu"),
    path('admin/', admin.site.urls),
    path('agencia/', include(('apps.agencia.urls', 'app_name'), namespace='agencia')),
    path('cliente/', include(('apps.cliente.urls', 'app_name'), namespace='cliente')),
    path('cat/', include('apps.catalog.urls')),
    path('api/', include('apps.agencia.api.urls')),
    path('api-cli/v1/', include('apps.apihc.urls')),
    path('api-dir/v1/', include('apps.direccion.urls')),
    path('api-obs/v1/', include('apps.observacion.urls')),
    path('api-vin/v1/', include('apps.vinculo.urls')),
    path('api-cue/v1/', include('apps.cuenta.urls')),
]