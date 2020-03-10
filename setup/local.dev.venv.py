from .settings import LOGGING

LOCAL_FILE_ROOT = ".local/venv"

SECRET_KEY = '00000000'
DEBUG = True
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': LOCAL_FILE_ROOT + '/db.sqlite3',
    }
}

# Change log path
LOGGING['handlers']['error_file']['filename'] = LOCAL_FILE_ROOT + "/error.log"
