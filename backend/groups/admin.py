from django.contrib import admin

from groups.models import Groups
from posts.models import Post

class GroupPostsInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ['text', 'image', 'tags', 'author']


@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupPostsInline, ]
    list_display = ['name', 'group_slug', 'title', 'image','is_closed_group', 'group_creator']