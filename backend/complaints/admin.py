from django.contrib import admin

from django.shortcuts import redirect, render
from django.urls import path

from complaints.models.complaints import Complaints
from complaints.models.comment_complaint import CommentComplaint
from complaints.models.group_complaint import GroupComplaint
from complaints.models.post_complaint import PostComplaint


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


@admin.register(GroupComplaint)
class GroupComplaintAdmin(ComplainAdmin):
    list_display = ['group'] + ComplainAdmin.list_display
