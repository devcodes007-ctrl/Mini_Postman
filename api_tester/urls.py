from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.api_info, name='api_info'),
    path('health/', views.health, name='health'),
]