from django.contrib import admin

from posts.models.post import Post
from posts.models.tag import Tag
from posts.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # TODO: Сделать так, чтобы при выборе поста в админке отображались
    #  комментарии которые относятся к нему.
    pass


admin.site.register(Post)
admin.site.register(Tag)