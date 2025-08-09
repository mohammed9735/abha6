from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from dotenv import load_dotenv

# ================================
# تحميل المتغيرات من ملف .env
# ================================
load_dotenv()

# ================================
# المسار الأساسي
# ================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================================
# مفاتيح الأمان ووضع التطوير
# ================================
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
DEBUG = os.getenv("DEBUG", "True") == "True"

# السماح بالنطاقات المحددة فقط في الإنتاج
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if not DEBUG else []

# ================================
# التطبيقات المثبتة
# ================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ تطبيقات المشروع
    'core',
    'products',
    'orders',
    'accounts',

    # ✅ Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ================================
# الوسطاء (Middlewares)
# ================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ Whitenoise: تقديم ملفات static في الإنتاج بدون إعدادات خارجية
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================================
# إعدادات الروابط والقوالب
# ================================
ROOT_URLCONF = 'abha6.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # المجلد العام للقوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'abha6.wsgi.application'

# ================================
# قاعدة البيانات (تطوير + إنتاج)
# ================================
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
        }
    }

# ================================
# التحقق من كلمات المرور
# ================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================================
# اللغة والتوقيت
# ================================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ================================
# الملفات الثابتة والميديا
# ================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]     # أثناء التطوير
STATIC_ROOT = BASE_DIR / "staticfiles"       # هدف collectstatic للإنتاج

# ✅ Whitenoise storage مع manifest + ضغط للملفات
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ✅ Cloudinary للملفات الإعلامية (media)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.getenv("CLOUDINARY_API_KEY"),
    'API_SECRET': os.getenv("CLOUDINARY_API_SECRET"),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# إجبار Cloudinary على قراءة الإعدادات (مفيد مع بعض البيئات)
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)

# ================================
# الإعدادات الافتراضية
# ================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ تعريف المستخدم المخصص
AUTH_USER_MODEL = 'accounts.CustomUser'
