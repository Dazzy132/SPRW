"""
Здесь нужно указывать модели для того, чтобы:
1) Создавались миграции
2) Их можно было импортировать из posts.models

Каждую новую модель нужно регистрировать в __all__ обязательно!
"""

from posts.models.post import Post
from posts.models.comment import Comment
from posts.models.tag import Tag
from posts.models.fields import LikesRelated, ViewsRelated

__all__ = [
    "Post",
    "Comment",
    "Tag",

    "LikesRelated",
    "ViewsRelated",
]