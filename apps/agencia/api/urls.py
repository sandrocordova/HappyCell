from django.urls import path
from apps.agencia.api.views import nav_infor_api_view, usernav_api_view, detail_view_set, cliente_api_view


urlpatterns = [
    #path('empresa', PostApiViewSetClass.as_view(), name='empresa_api'),
    path('usernav', usernav_api_view, name='api_user_nav'),
    path('usernavdos', nav_infor_api_view, name='api_user_nav_dos'),
    path('empresa', detail_view_set, name='api_empresa'),
    path('cliente', cliente_api_view, name='api_cliente'),
    #path('empresa/<int:pk>', detail_view_set, name='empresa_api_id'),
]
