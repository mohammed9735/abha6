# accounts/managers.py
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("البريد الإلكتروني مطلوب")
        if not phone_number:
            raise ValueError("رقم الجوال مطلوب")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser يجب أن يكون is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser يجب أن يكون is_superuser=True")

        return self.create_user(username, email, phone_number, password, **extra_fields)
