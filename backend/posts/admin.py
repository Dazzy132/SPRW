from django.contrib import admin

from posts.models import Comment, Post, Tag


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
    # exclude = ['comments']
    inlines = [PostCommentsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['post'].disabled = True
        return form

    class Media:
        js = ('script.js',)


admin.site.register(Tag)
