from datetime import timedelta

AUTH_USER_MODEL = 'users.User'

ACCOUNT_AUTHENTICATION_METHOD = 'email | username'
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
    'JWT_AUTH_COOKIE': 'SPRW-AUTH',
    'USE_JWT': True,
    'REGISTER_SERIALIZER': 'a12n.api.serializers.CustomRegisterSerializer',
}

# JWT_AUTH = {
#     "JWT_EXPIRATION_DELTA": timedelta(days=14),
#     "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=21),
#     "JWT_ALLOW_REFRESH": True,
#     "JWT_ISSUER": "education-backend",
#     "JWT_ALGORITHM": "RS256",
#     "JWT_PAYLOAD_HANDLER": "a12n.jwt.payload_handler",
# }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
