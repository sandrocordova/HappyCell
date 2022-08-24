from django.urls import path

from .views import DireccionView, TelefonoView

urlpatterns = [
    path('direccion', DireccionView.as_view()),
    path('telefono', TelefonoView.as_view()),
]
