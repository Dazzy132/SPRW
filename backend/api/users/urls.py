from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import index

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('test/', index, name='test'),
]