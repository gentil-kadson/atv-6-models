from django.urls import path
from apps.sebo_de_discos import views

urlpatterns = [
    path('', views.index, name='home')
]