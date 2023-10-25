from django.urls import path
from apps.sebo_de_discos import views

urlpatterns = [
    path('', views.index, name='home'),
    path('disco/<int:id_disco>/', views.disco, name='disco'),
    path('cadastrar-disco/', views.cadastrar_disco, name='cadastrar_disco')
]