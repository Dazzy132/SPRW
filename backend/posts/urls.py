from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.api import views

router = DefaultRouter()
router.register(r'tags', views.TagViewSet, basename='tags')
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                views.CommentViewSet, basename='comments')
router.register(r'likes', views.UserLikesViewSet, basename='likes')


urlpatterns = [
    path('', include(router.urls)),
]