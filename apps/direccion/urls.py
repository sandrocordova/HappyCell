from django.urls import path

from .views import DireccionView, TelefonoView, direccionSearch, telefonoSearch

urlpatterns = [
    path('direccion', DireccionView.as_view()),
    path('telefono', TelefonoView.as_view()),
    path('dir-search', direccionSearch.as_view()),
    path('tel-search', telefonoSearch.as_view()),
]
