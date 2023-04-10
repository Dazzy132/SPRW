from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chats.api.views import MessageViewSet, ChatViewSet

router = DefaultRouter()
router.register(r"", ChatViewSet, basename="chats")
router.register(r"(?P<user_id>\d+)/messages", MessageViewSet, basename="messages")


urlpatterns = [
    path("", include(router.urls)),
]