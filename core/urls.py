from django.urls import path
from .views import get_endpoint_data

urlpatterns = [
    path('api/', get_endpoint_data, name='get_endpoint_data'),
]