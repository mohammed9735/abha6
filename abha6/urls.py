from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),           # الصفحة الرئيسية
    path('products/', include('products.urls')),  # المنتجات
    path('orders/', include('orders.urls')),      # الطلبات
    path('accounts/', include('accounts.urls')),  # تسجيل الدخول والتسجيل
]

# ✅ دعم media و static أثناء التطوير وبعد تجميع الملفات الثابتة
if settings.DEBUG:
    # عرض الصور والملفات المرفوعة من media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # عرض الملفات الثابتة (CSS, JS) سواء من static أو staticfiles بعد collectstatic
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
