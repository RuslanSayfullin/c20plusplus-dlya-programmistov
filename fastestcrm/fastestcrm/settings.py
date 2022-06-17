import os
from pathlib import Path
from .settings_db_debug import DEBUG, DATABASES  # импорт настроект "режима отладки" и "базы данных"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h9$rb%r)z8xjoom+qh2!9@*j_*x8p8xm+r1o1ll%yd!wec6k5d'

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ("127.0.0.1",)   # кортеж с перечнем IP-адресов, с которых может вестись разработка.

INTERNAL_IPS = (
    "127.0.0.1",
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',          # Система аутентификации
    'django.contrib.contenttypes',  # Система типов контента
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',      # Набор фильтров шаблонов Django, для придания данным «человеческого оттенка».
    'debug_toolbar',                # Набор панелей, появляющихся на странице в режиме отладки
    'rest_framework',               # API интерфейс
] + [
     'inquery.apps.InqueryConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',      # Набор панелей, появляющихся на странице в режиме отладки
]

ROOT_URLCONF = 'fastestcrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'fastestcrm.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'                      # URL для шаблонов
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')        # "Поисковики" статики. Ищет статику в STATICFILES_DIRS.
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'       # Абсолютный путь в файловой системе, с каталогом, где файлы, загруженные пользователями.

DATA_UPLOAD_MAX_MEMORY_SIZE = 157286400    # Максимальный размер тела запроса в байтах (150 МБ).
FILE_UPLOAD_MAX_MEMORY_SIZE = 157286400    # Макс. размер (в байтах) загрузки до ее депортации в файл. систему (150 МБ).

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
