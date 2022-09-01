from django.urls import path

from .views import getToken, validate

urlpatterns = [
    path('token', getToken.as_view()),
    path('validate', validate.as_view()),
    #path('cliente', CLIENTESView.as_view()),
]
