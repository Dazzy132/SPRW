from django.urls import include, path

urlpatterns = [
    path('auth/', include("a12n.urls")),
    path('users/', include("users.urls")),
    path('', include("posts.urls")),
]
