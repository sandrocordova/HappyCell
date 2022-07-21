from django.urls import path
from apps.agencia.api.views import PostApiViewSet


urlpatterns = [
    path('empresa', PostApiViewSet.as_view(), name='empresa_api'),
]
