from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path

from posts.models import (Comment, CommentComplaint, Complaints, Post,
                          PostComplaint, PostLike, Tag)


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

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['post'].disabled = True
        return form

    class Media:
        js = ('script.js',)


class ComplainAdmin(admin.ModelAdmin):
    list_display = ['id', 'complaint', 'complaint_status', 'user']
    actions = ['change_status']

    @admin.action(description='Изменить статус жалобы')
    def change_status(self, request, *args, **kwargs):
        queryset = self.get_queryset(request)
        print(request)
        if 'apply' in request.POST:
            status = request.POST.get('status')
            if status:
                queryset.update(complaint_status=status)
                return redirect(request.META.get('HTTP_REFERER'))

        context = {
            'queryset': queryset,
            'status_choices': Complaints.COMPLAINT_STATUS_CHOISE,
        }
        return render(request, 'admin/change_status.html', context=context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('change-status/',
                 self.admin_site.admin_view(self.change_status),
                 name='change_status'),
        ]
        return custom_urls + urls


@admin.register(CommentComplaint)
class CommentComplaintAdmin(ComplainAdmin):
    list_display = ['comment'] + ComplainAdmin.list_display


@admin.register(PostComplaint)
class PostComplaintAdmin(ComplainAdmin):
    list_display = ['post'] + ComplainAdmin.list_display


admin.site.register(Tag)
admin.site.register(PostLike)
