from django.urls import path, include

from . import views

# namespace
app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.shop, name='shop'),
    path('about_me/', views.about_me, name='about_me'),
]
