from django.urls import path
from . import views

urlpatterns = [
    # صفحة مؤقتة للطلبات
    path('', views.orders_home, name='orders_home'),
]
