from django.urls import path

from complaints.api import views


urlpatterns = [
    path('commentcomplaint/create/',
         views.CommentComplaintCreateAPIView.as_view(),
         name='comment_complaint_create'),
    path('groupcomplaint/create/',
         views.GroupComplaintCreateAPIView.as_view(),
         name='group_complaint_create'),
    path('postcomplaint/create/',
         views.PostComplaintCreateAPIView.as_view(),
         name='post_complaint_create'),
    path('profilecomplaint/create/',
         views.ProfileComplaintCreateAPIView.as_view(),
         name='profile_complaint_create')
]
