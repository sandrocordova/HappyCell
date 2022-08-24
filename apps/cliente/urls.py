from django.urls import path
from apps.cliente.views import ClienteView, cliente_api_view, cliente_search, direccion_search



urlpatterns = [
    path('view', cliente_api_view, name='api_cliente'),
    path('search', cliente_search.as_view()),
    path('/dir/search', direccion_search.as_view()),
    path('/cliente', ClienteView.as_view()),
    #path('empresa/<int:pk>', detail_view_set, name='empresa_api_id'),
]
