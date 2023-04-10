"""
Здесь нужно указывать модели для того, чтобы:
1) Создавались миграции
2) Их можно было импортировать из posts.models

Каждую новую модель нужно регистрировать в __all__ обязательно!
"""

from posts.models.comment import Comment
from posts.models.complaints import Complaints, CommentComplaint, PostComplaint
from posts.models.fields import LikesRelated, ViewsRelated
from posts.models.post import Post, PostLike
from posts.models.tag import Tag
from posts.models.complaints import Complaints, CommentComplaint, PostComplaint


__all__ = [
    "Post",
    "PostLike",
    "Comment",
    "Complaints",
    "CommentComplaint",
    "PostComplaint",
    "Tag",

    "LikesRelated",
    "ViewsRelated",
]