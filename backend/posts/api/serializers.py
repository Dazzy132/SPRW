from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Comment, Post, PostLike, Tag

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
        many=True, read_only=True, source="comments"
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
    is_liked = None

    def to_representation(self, instance):
        return PostGETSerializer(instance).data

    class Meta:
        model = Post
        fields = "__all__"
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


class UserLikeCreateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        is_liked = attrs["user"].posts_postlike_user.filter(
            post=attrs["post"]
        ).exists()

        if self.context.get("request").method == "POST":
            if is_liked:
                raise serializers.ValidationError("Вы уже поставили лайк")

        if self.context.get("request").method == "DELETE":
            if not is_liked:
                raise serializers.ValidationError(
                    "Вы не можете убрать лайк которого нет"
                )

        return attrs

    class Meta:
        model = PostLike
        fields = [
            "user", "post", "created"
        ]