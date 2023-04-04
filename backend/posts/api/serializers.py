from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Comment, Post, Tag

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class CommentGETSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    image = Base64ImageField(required=False)

    class Meta:
        model = Comment
        fields = "__all__"


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

    class Meta:
        model = Post
        fields = [
            "id", "uuid", "author", "text", "likes", "views", "comments",
            "image", "tags", "created", "modified",
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
