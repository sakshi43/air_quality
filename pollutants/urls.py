# pollutants/urls.py
from django.urls import path
from .views import pollutants_data

urlpatterns = [
    path('pollutants/', pollutants_data, name='pollutant_data'),
]
