from django.contrib import admin

from posts.models import (Comment, Post,
                          PostLike, Tag)


class PostCommentsInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = [
        "author",
        "text",
        "image"
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ['comments']
    inlines = [PostCommentsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'image', 'id')
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if obj:
    #         form.base_fields['post'].disabled = True
    #     return form

    # class Media:
    #     js = ('script.js',)


admin.site.register(Tag)
admin.site.register(PostLike)
