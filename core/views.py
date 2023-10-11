from django.shortcuts import render

from product.models import Product, Category

def homepage(request):
    featured_products = Product.objects.all()[:4]
    categories = Category.objects.all()[:4]
    new_arrival_products = Product.objects.all()[:4]

    return render(request, 'core/homepage.html', {
        'featured_products': featured_products,
        'categories': categories,
        'new_arrival_products': new_arrival_products,
        
    })

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "core/shop.html", {
        'products': products,
        'categories':categories,
    })

def about_me(request):

    return render(request, 'core/about_me.html')