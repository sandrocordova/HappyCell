from django.urls import path

from .views import CuentaBancariaView

urlpatterns = [
    path('cuenta', CuentaBancariaView.as_view()),
]
