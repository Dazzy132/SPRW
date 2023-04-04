from django.urls import path, include


urlpatterns = [
    path('auth/', include("a12n.urls")),
    path('', include("posts.urls")),
]
