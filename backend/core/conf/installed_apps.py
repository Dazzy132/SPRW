INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    # Улучшенная версия shell
    'django_extensions',

    # Установленные пакеты
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # Приложения Django
    'a12n.apps.A12NConfig',
    'users.apps.UsersConfig',
    'posts.apps.PostsConfig',
]