from django.urls import path
from .views import *

app_name = 'members'

urlpatterns = [
    path('bancos/', BancoListView.as_view(), name='bancos-list'),
    path('bancos/<int:pk>/', BancoDetailView.as_view(), name='banco-detail'),
    path('bancos/nuevo/', BancoCreateView.as_view(), name='banco-create'),
    path('bancos/<int:pk>/editar/', BancoUpdateView.as_view(), name='banco-update'),
    path('bancos/<int:pk>/eliminar/', BancoDeleteView.as_view(), name='banco-delete'),
    
    
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente-delete'),
    
    
    path('creditos/', CreditoListView.as_view(), name='credito-list'),
    path('creditos/<int:pk>/', CreditoDetailView.as_view(), name='credito-detail'),
    path('creditos/nuevo/', CreditoCreateView.as_view(), name='credito-create'),

]