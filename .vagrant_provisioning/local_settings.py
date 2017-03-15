DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scw',
        'USER': 'scw',
        'PASSWORD': 'scw',
        'ADMINUSER': 'postgres',
        'HOST': 'localhost'
    },
}

INTERNAL_IPS = ('0.0.0.0', '127.0.0.1', '::1')

SECRET_KEY = '12345'

FABRIC_USER = ''

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
