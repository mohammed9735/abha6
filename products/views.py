from django.shortcuts import render
from .models import Product

def products_home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products/products_list.html', {'products': products})
