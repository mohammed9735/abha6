from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),          # الصفحة الرئيسية
    path('products/', include('products.urls')),  # المنتجات
    path('orders/', include('orders.urls')),      # الطلبات
    path('accounts/', include('accounts.urls')),  # تسجيل الدخول والتسجيل
]

# ✅ إضافة دعم عرض الصور المرفوعة (MEDIA)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
