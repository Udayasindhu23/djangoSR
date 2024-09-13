from django.urls import path
from .views import predict_health

urlpatterns = [
    path('', predict_health, name='predict_health'),
]
