from django.urls import path

from .views import VinculoView, vinculoSearch

urlpatterns = [
    path('vinculo', VinculoView.as_view()),
    path('vin-search', vinculoSearch.as_view()),
]
