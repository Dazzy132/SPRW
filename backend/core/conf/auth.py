from datetime import timedelta

AUTH_USER_MODEL = 'users.User'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_ADAPTER = 'a12n.adapter.MyAccountAdapter'

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

REST_AUTH = {
    'USE_JWT': True,
    "JWT_AUTH_HTTPONLY": False,
    'JWT_AUTH_COOKIE': 'SPRW-AUTH',
    'JWT_AUTH_RETURN_EXPIRATION': True,
    'JWT_AUTH_REFRESH_COOKIE': "my-refresh-cookie",
    'REGISTER_SERIALIZER': 'a12n.api.serializers.CustomRegisterSerializer',
    "PASSWORD_RESET_SERIALIZER": "a12n.api.serializers.CustomPasswordResetSerializer",
    "OLD_PASSWORD_FIELD_ENABLED": True,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=14),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
    {'NAME': 'a12n.validators.NoSpacesPasswordValidator',},
]
