from split_settings.tools import include

from core.conf.envrion import env

SECRET_KEY = env("SECRET_KEY", cast=str, default="s3cr3t")
DEBUG = env("DEBUG")

include(
    "conf/base.py",
    "conf/installed_apps.py",
    "conf/middleware.py",
    "conf/templates.py",
    "conf/db.py",
    "conf/i18n.py",
    "conf/static.py",
    "conf/media.py",
    "conf/http.py",
    "conf/timezone.py",
    "conf/email.py",
    "conf/api.py",
    "conf/auth.py",
    "conf/debug_toolbar.py",
    "conf/smart_selects.py",
    "conf/jet-admin.py",
    "conf/cors.py",
)
