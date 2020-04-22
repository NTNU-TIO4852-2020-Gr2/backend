SECRET_KEY = "00000000"
DEBUG = True
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

DATABASES = {
    #"default": {
    #    "ENGINE": "django.db.backends.sqlite3",
    #    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    #},
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "eit",
        "USER": "eit",
        "PASSWORD": "eit",
        "HOST": "db",
    },
}
