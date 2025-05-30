from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro, Carrito, ItemCarrito, Pedido, ItemPedido
from django.contrib.auth.decorators import login_required

def catalogo(request):
    carros = Carro.objects.filter(disponible=True)
    carrito = None
    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(cliente=request.user)
    return render(request, 'renta/catalogo.html', {'carros': carros, 'carrito': carrito})



@login_required
def agregar_carrito(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    carrito, creado = Carrito.objects.get_or_create(cliente=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, carro=carro)
    if not creado:
        item.cantidad += 1
    item.save()
    return redirect('catalogo')

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(cliente=request.user)
    return render(request, 'renta/carrito.html', {'carrito': carrito})

@login_required
def quitar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def colocar_pedido(request):
    carrito = get_object_or_404(Carrito, cliente=request.user)
    
    if request.method == 'POST':
        for item in carrito.items.all():
            fecha_inicio = request.POST.get(f'fecha_inicio_{item.id}')
            fecha_fin = request.POST.get(f'fecha_fin_{item.id}')
            
            item.fecha_inicio = fecha_inicio
            item.fecha_fin = fecha_fin
            item.save()
        
        pedido = Pedido.objects.create(cliente=request.user)
        for item in carrito.items.all():
            ItemPedido.objects.create(
                pedido=pedido,
                carro=item.carro,
                cantidad=item.cantidad,
                fecha_inicio=item.fecha_inicio,
                fecha_fin=item.fecha_fin
            )
        carrito.items.all().delete()
        return redirect('catalogo')
    
    return redirect('ver_carrito')
