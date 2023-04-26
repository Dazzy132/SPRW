from django.urls import include, path

urlpatterns = [
    path('auth/', include("a12n.urls")),
    path('chats/', include("chats.urls")),
    path('', include("users.urls")),
    path('', include("posts.urls")),
    path('', include("groups.urls"))
]
