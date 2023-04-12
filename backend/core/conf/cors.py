from core.conf.envrion import env
from core.conf.middleware import MIDDLEWARE

if env("DEBUG"):
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
    )
    MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware', ]
