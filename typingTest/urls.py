from django.urls import path
from . import views

urlpatterns = [
    path('', views.typing_test, name='typing-test'),
]