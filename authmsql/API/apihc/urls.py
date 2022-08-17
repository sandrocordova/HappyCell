from django.urls import path

from .views import getToken, validate, cliente

urlpatterns = [
    path('token', getToken.as_view()),
    path('validate', validate.as_view()),
    path('cliente', cliente.as_view()),
]
