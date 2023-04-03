from datetime import timedelta
import os
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    # Установленные пакеты
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # Приложения Django
    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    'api.users.apps.UsersConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# ---------------------------- Настройки проекта ----------------------------

AUTH_USER_MODEL = 'users.User'
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1

# ---------------------------- Настройки проекта ----------------------------


# ---------------------------- Настройки перевода ----------------------------

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


def gettext_domain(s):
    """Функция для получения значений домена"""
    return s


LANG_DOMAINS = [
    gettext_domain('django'),
    gettext_domain('django.contrib.admin'),
]

# ---------------------------- Настройки перевода ----------------------------


# ---------------------------- Настройки статики ----------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ---------------------------- Настройки статики ----------------------------


# ------------------------- Настройки аутентификации -------------------------

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

ACCOUNT_AUTHENTICATION_METHOD = 'email | username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_ADAPTER = 'api.users.adapter.MyAccountAdapter'

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
}

REST_AUTH = {
    'JWT_AUTH_COOKIE': 'SPRW-AUTH',
    'USE_JWT': True,
    'REGISTER_SERIALIZER': 'api.users.serializers.CustomRegisterSerializer',
}

# ------------------------- Настройки аутентификации -------------------------