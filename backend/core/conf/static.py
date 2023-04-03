import os.path

from core.conf.base import BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')