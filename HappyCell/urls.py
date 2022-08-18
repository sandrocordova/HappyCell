from django.contrib import admin
from django.urls import path, include
from HappyCell.view import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.agencia.api.urls')),
    path('agencia/', include(('apps.agencia.urls', 'app_name'), namespace='agencia')),
    path('cliente/', include(('apps.cliente.urls', 'app_name'), namespace='cliente')),
    path('cat/', include('apps.catalog.urls')),
    path('', menu, name="menu"),
    path('api-cli/v1/', include('apps.apihc.urls')),
]