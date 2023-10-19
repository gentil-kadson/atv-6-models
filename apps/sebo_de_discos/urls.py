from django.urls import path
from apps.sebo_de_discos import views

urlpatterns = [
    path('', views.index, name='home'),
    path('disco/<int:id_disco>/', views.disco, name='disco')
]