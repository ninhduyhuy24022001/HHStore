from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from product.models import Product, Category
from order.models import Order, OrderItem
from .forms import SignupFrom

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

    search = request.GET.get('search', '')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))


    active_category = request.GET.get('category' ,'')
    if active_category:
        products = products.filter(category__slug=active_category)
    

    return render(request, "core/shop.html", {
        'products': products,
        'categories':categories,
        'active_category': active_category,
    })

def about_me(request):

    return render(request, 'core/about_me.html')

def signup(request):
    if request.method == "POST":
        form = SignupFrom(request.POST)

        if form.is_valid:
            form.save()

            return redirect('/login/')

    else:
        form = SignupFrom()

    return render(request, 'core/signup.html', {
        'form': form,
    })
    

@login_required
def myaccount(request):
    
    return render(request, 'core/myaccount.html')