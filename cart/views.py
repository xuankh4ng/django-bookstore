from django.shortcuts import redirect, render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products
    quantity = cart.get_quantity
    total = cart.cart_total()
    return render(request, 'cart_summary.html', {"cart_products": cart_products, "quantity": quantity, "total": total})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity=product_quantity)

        cart_quantity = cart.__len__()

        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'Quantity': cart_quantity})
        return response

def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product=product_id, quantity=product_quantity)
        response = JsonResponse({'Quantity': product_quantity})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        response = JsonResponse({'Product': product_id})
        return response
