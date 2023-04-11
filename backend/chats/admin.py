from django.contrib import admin

from chats.models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message)
