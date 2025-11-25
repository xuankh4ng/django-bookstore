from django.shortcuts import render
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, cate_name):
    cate_name = cate_name.replace('-', ' ')

    try:
        category = Category.objects.get(name=cate_name)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'category': category, 'products': products})
    except:
        return redirect('home')
