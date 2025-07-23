from django.shortcuts import render
from products.models import Product

def home(request):
    # جلب آخر 6 منتجات لعرضها في الصفحة الرئيسية كبنر
    products = Product.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'products': products})
