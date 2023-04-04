from django.core.cache import cache
from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Comment, Post, Tag

from .serializers import (CommentCreateSerializer, CommentGETSerializer,
                          PostCreateSerializer, PostGETSerializer,
                          TagSerializer)


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Кеширование для предотвращения накрутки просмотров
        user_key = f"user_{request.user.pk}"
        post_key = f"post_{instance.pk}"
        if cache.get(f"{user_key}_{post_key}") is None:
            instance.views = F('views') + 1
            instance.save()
            instance.refresh_from_db()
            cache.set(f"{user_key}_{post_key}", True, timeout=60)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        return (
            Post.objects
            .select_related('author')
            .prefetch_related("tags", "comments__author")
        )

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return PostGETSerializer
        return PostCreateSerializer


class CommentViewSet(ModelViewSet):

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        return (
            Comment.objects
            .filter(post=self.get_post())
            .select_related('author', 'post')
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.get_post().pk)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return CommentGETSerializer
        return CommentCreateSerializer