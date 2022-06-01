import sys

from decouple import config

from .base import BASE_DIR

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "test_db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME", default="postgres"),
            "USER": config("DB_USER", default="postgres"),
            "PASSWORD": config("DB_PASSWORD", default="password"),
            "HOST": config("DB_HOST", default="localhost"),
            "PORT": config("DB_PORT", default=5432),
            "OPTIONS": {"options": "-c search_path=%s" % config("DB_SCHEMA", default="public")},
        }
    }
