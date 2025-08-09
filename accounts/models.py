from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager  # تأكد من وجود managers.py كما بالخطوة 1

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="رقم الجوال")

    # يطلب هذه الحقول في createsuperuser إلى جانب username
    REQUIRED_FIELDS = ["email", "phone_number"]  # لا تغيّر USERNAME_FIELD (يبقى username)

    # ربط الـ Manager المخصص
    objects = CustomUserManager()

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username
