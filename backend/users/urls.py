from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.api.views import ProfileViewSet, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"profile", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
]
