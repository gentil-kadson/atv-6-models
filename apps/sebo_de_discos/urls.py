from django.urls import path
from apps.sebo_de_discos import views

urlpatterns = [
    path('', views.index, name='home'),
    path('disco/<int:id_disco>/', views.disco, name='disco'),
    path('cadastrar-disco/', views.cadastrar_disco, name='cadastrar_disco'),
    path('remover-disco/<int:id_disco>/', views.remover_disco, name="remover_disco"),
    path('editar-disco/<int:id_disco>/', views.editar_disco, name="editar_disco")
]