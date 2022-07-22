from django.urls import path
from apps.agencia.api.views import PostApiViewSet, nav_api_view


urlpatterns = [
    #path('empresa', PostApiViewSetClass.as_view(), name='empresa_api'),
    path('info', nav_api_view, name='api_nav'),
    path('empresa/<int:id>', PostApiViewSet.as_view(), name='empresa_api_id'),
]
