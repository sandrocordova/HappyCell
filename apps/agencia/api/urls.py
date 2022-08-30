from django.urls import path
from apps.agencia.api.views import nav_infor_api_view, usernav_api_view, detail_view_set

urlpatterns = [
    path('user-data', usernav_api_view, name='api_user_nav'),
    path('user-nav-menu', nav_infor_api_view, name='api_user_nav_dos'),
    path('empresa', detail_view_set, name='api_empresa'),
]
