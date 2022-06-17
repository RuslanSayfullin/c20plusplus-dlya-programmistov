"""
Django settings for DATABASES and DEBUG.
"""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fastestcrm',
        'USER': 'portaluser',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

