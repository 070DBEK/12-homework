from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'products/about.html')

def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request, 'products/product-list.html', ctx)


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        if name and description and price and image and category:
            Product.objects.create(
                name = name,
                description = description,
                price = price,
                image = image,
                category = category
            )
            return redirect('home')
    return render(request, 'products/product-create.html')

def product_detail(request, detail_id):
    products = get_object_or_404(Product, pk=detail_id)
    ctx = {'products': products}
    return render(request, 'products/product-detail.html', ctx)
