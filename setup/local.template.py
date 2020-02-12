# Set to a randomly generated key in production
SECRET_KEY = ''

# Disable in production
DEBUG = False

# Set to the domain name(s)
ALLOWED_HOSTS = [
    'example.net'
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Security
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
