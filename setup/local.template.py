import os

# Settings directory
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
# Root directory
BASE_DIR = os.path.normpath(os.path.join(SETTINGS_DIR, '..', '..'))

# Set to a randomly generated key in production
SECRET_KEY = ''

# Disable in production
DEBUG = False

# Set to the domain name(s)
ALLOWED_HOSTS = [
    'example.net'
]

# Database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Security
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Map
GOOGLE_MAPS_API_KEY = ""
GOOGLE_MAPS_LATITUDE = "63.419499"
GOOGLE_MAPS_LONGITUDE = "10.402077"
GOOGLE_MAPS_ZOOM = "10"
# roadmap, satellite, hybrid or terrain
GOOGLE_MAPS_TYPE = "terrain"

# API
API_MEASUREMENTS_MAX_COUNT = 1000
