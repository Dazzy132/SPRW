import os.path

from core.conf.base import BASE_DIR
from core.conf.envrion import env

if env("DEBUG"):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')