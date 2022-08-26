from django.urls import path
from apps.catalog.views import catalog_api_views


urlpatterns = [
    path('view', catalog_api_views.as_view()),
]
