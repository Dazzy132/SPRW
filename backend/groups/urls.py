from django.urls import include, path
from rest_framework.routers import DefaultRouter

from groups.api.views import GroupViewSet

router = DefaultRouter()
router.register(r"groups", GroupViewSet, basename="groups")

urlpatterns = [
    path("", include(router.urls)),
]