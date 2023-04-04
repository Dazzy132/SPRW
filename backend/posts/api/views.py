from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import PostGETSerializer, PostCreateSerializer, CommentGETSerializer, CommentCreateSerializer, TagSerializer
from posts.models import Post, Comment, Tag


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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