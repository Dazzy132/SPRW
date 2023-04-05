from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Comment, Post, Tag, PostLike

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для представления Тегов"""

    class Meta:
        model = Tag
        fields = "__all__"


class CommentGETSerializer(serializers.ModelSerializer):
    """Данный сериализатор подходит только для HTTP GET запросов и не
    поддерживает создание или обновление объектов Comment. """

    author = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    image = Base64ImageField(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'image', 'parent',)


class CommentCreateSerializer(CommentGETSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )

    def create(self, validated_data):
        post = validated_data.pop('post')
        comment = Comment.objects.create(**validated_data)
        post.comments.add(comment)
        return comment

    class Meta:
        model = Comment
        fields = [
            "post", "text", "image", "parent"
        ]


class PostGETSerializer(serializers.ModelSerializer):
    """Сериализатор Постов только для GET запросов"""
    author = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    image = Base64ImageField(
        required=False
    )
    comments = CommentGETSerializer(
        many=True
    )
    tags = TagSerializer(
        many=True
    )
    is_liked = serializers.BooleanField(default=False)

    class Meta:
        model = Post
        fields = [
            "id", "uuid", "author", "text", "likes", "is_liked", "views",
            "comments", "image", "tags", "created", "modified",
        ]


class PostCreateSerializer(PostGETSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Tag.objects.all(),
    )
    # Комментарии на момент создания поста не нужны
    comments = None

    def to_representation(self, instance):
        return PostGETSerializer(instance).data

    class Meta:
        model = Post
        exclude = ["comments"]
        read_only_fields = [
            "uuid", "likes", "views", "modified",
        ]


class UserLikesGetSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        "username",
        queryset=User.objects.all()
    )

    class Meta:
        model = PostLike
        fields = "__all__"