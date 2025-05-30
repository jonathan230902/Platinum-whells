from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('agregar_carrito/<int:carro_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('colocar_pedido/', views.colocar_pedido, name='colocar_pedido'),
    path('quitar_item/<int:item_id>/', views.quitar_item, name='quitar_item'),
]
