from django.urls import path

from .views import ObservacionClienteView

urlpatterns = [
    path('observacion', ObservacionClienteView.as_view()),
]
