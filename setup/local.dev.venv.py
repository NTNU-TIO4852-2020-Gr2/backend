# Set to a randomly generated key in production
SECRET_KEY = '00000000'

# Disable in production
DEBUG = True

# Set to the domain name(s)
ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
