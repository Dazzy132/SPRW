from django.urls import include, path

urlpatterns = [
    path('auth/', include("a12n.urls")),
    path('', include("posts.urls")),
]
