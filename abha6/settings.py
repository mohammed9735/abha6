from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ================================
# المسار الأساسي
# ================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================================
# مفاتيح الأمان ووضع التطوير
# ================================
SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
DEBUG = True
ALLOWED_HOSTS = []

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
# قاعدة البيانات
# ================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
STATIC_ROOT = BASE_DIR / "staticfiles"       # بعد جمع الملفات عبر collectstatic

# ✅ إعداد Cloudinary للملفات الإعلامية
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dto3fm08p',  # ضع قيمتك الخاصة
    'API_KEY': '926795448327751',  # ضع قيمتك الخاصة
    'API_SECRET': 'GTr7Ib8lQ2JXM9yECQHWmWVGG6Y',  # ضع قيمتك الخاصة
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ✅ إجبار مكتبة Cloudinary على قراءة الإعدادات تلقائيًا
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
