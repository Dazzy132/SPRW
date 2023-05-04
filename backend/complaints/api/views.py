from rest_framework.generics import CreateAPIView

from complaints.api.serializers import (CommentComplaintSerializer,
                                        GroupComplaintSerializer,
                                        PostComplaintSerializer,
                                        ProfileComplaintSerializer)
from complaints.models.comment_complaint import CommentComplaint
from complaints.models.group_complaint import GroupComplaint
from complaints.models.post_complaint import PostComplaint
from complaints.models.profile_complaint import ProfileComplaint


class CommentComplaintCreateAPIView(CreateAPIView):
    serializer_class = CommentComplaintSerializer
    queryset = CommentComplaint.objects.all()


class GroupComplaintCreateAPIView(CreateAPIView):
    serializer_class = GroupComplaintSerializer
    queryset = GroupComplaint.objects.all()


class PostComplaintCreateAPIView(CreateAPIView):
    serializer_class = PostComplaintSerializer
    queryset = PostComplaint.objects.all()


class ProfileComplaintCreateAPIView(CreateAPIView):
    serializer_class = ProfileComplaintSerializer
    queryset = ProfileComplaint.objects.all()
