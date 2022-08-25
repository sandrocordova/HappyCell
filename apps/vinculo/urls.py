from django.urls import path

from .views import VinculoView

urlpatterns = [
    path('vinculo', VinculoView.as_view()),
]
