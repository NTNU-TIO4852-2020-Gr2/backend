import os

# Settings directory
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
# Root directory
BASE_DIR = os.path.normpath(os.path.join(SETTINGS_DIR, "..", ".."))

# Set to a randomly generated key in production
SECRET_KEY = ""

# Disable in production
DEBUG = False

# Set to the domain name(s)
ALLOWED_HOSTS = [
    "example.net"
]

# Database
#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#    }
#}

# Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

# Security
CSRF_COOKIE_PATH = "/"
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# API
API_MEASUREMENTS_MAX_COUNT = 1000

# Misc
LOGO_LINK = "/"
