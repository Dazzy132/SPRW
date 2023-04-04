from django.contrib import admin
from django.utils.html import format_html

from posts.models.post import Post
from posts.models.tag import Tag
from posts.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['post'].disabled = True
        return form

    class Media:
        js = ('script.js',)


admin.site.register(Post)
admin.site.register(Tag)
