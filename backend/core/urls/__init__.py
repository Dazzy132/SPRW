from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

api = [
    path("v1/", include("core.urls.v1"))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls))
    ]

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )