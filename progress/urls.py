from django.urls import path
from . import views

urlpatterns = [
    path('', views.life_progress, name='life_progress'),
]