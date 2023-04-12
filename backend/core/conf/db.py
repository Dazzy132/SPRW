import os.path

from core.conf.base import BASE_DIR
from core.conf.envrion import env

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if env('DEBUG'):
    DATABASES = {
        "default": {
            "ENGINE": os.getenv("DB_ENGINE", default="django.db.backends.postgresql"),
            "NAME": os.getenv("DB_NAME", default="party_project"),
            "USER": os.getenv("POSTGRES_USER", default="Admin"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="Admin"),
            "HOST": os.getenv("DB_HOST", default="127.0.0.1"),
            "PORT": os.getenv("DB_PORT", default="5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("DB_NAME", default="postgres"),
            "USER": os.getenv("POSTGRES_USER", default="postgres"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
            "HOST": os.getenv("DB_HOST", default="db"),
            "PORT": os.getenv("DB_PORT", default="5432"),
        }
    }
