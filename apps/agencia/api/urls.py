from django.urls import path
from apps.agencia.api.views import nav_infor_api_view, usernav_api_view, detail_view_set, cliente_api_view, profesiones_api_views
from apps.agencia.api.views import profesiones_api_views, nacionalidad_api_views, acti_economica_api_views, tipo_rol_api_views, sexo_api_views, vivienda_api_views, estado_civil_api_views, situacion_laboral_api_views


urlpatterns = [
    #path('empresa', PostApiViewSetClass.as_view(), name='empresa_api'),
    path('usernav', usernav_api_view, name='api_user_nav'),
    path('usernavdos', nav_infor_api_view, name='api_user_nav_dos'),
    path('empresa', detail_view_set, name='api_empresa'),
    path('cliente', cliente_api_view, name='api_cliente'),
    path('cat/1', profesiones_api_views.as_view()),
    path('cat/2', nacionalidad_api_views.as_view()),
    path('cat/3', acti_economica_api_views.as_view()),
    path('cat/4', tipo_rol_api_views.as_view()),
    path('cat/5', sexo_api_views.as_view()),
    path('cat/6', vivienda_api_views.as_view()),
    path('cat/7', estado_civil_api_views.as_view()),
    path('cat/8', situacion_laboral_api_views.as_view()),
    #path('empresa/<int:pk>', detail_view_set, name='empresa_api_id'),
]
