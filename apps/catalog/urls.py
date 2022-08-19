from django.urls import path
from apps.catalog.views import profesiones_api_views, nacionalidad_api_views, acti_economica_api_views, tipo_rol_api_views, sexo_api_views, vivienda_api_views, estado_civil_api_views, situacion_laboral_api_views
from apps.catalog.views import catalog_api_views


urlpatterns = [
    path('1', profesiones_api_views.as_view()),
    path('2', nacionalidad_api_views.as_view()),
    path('3', acti_economica_api_views.as_view()),
    path('4', tipo_rol_api_views.as_view()),
    path('5', sexo_api_views.as_view()),
    path('6', vivienda_api_views.as_view()),
    path('7', estado_civil_api_views.as_view()),
    path('8', situacion_laboral_api_views.as_view()),
    path('view', catalog_api_views.as_view()),
]
