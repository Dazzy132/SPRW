from rest_framework import serializers

from complaints.models.comment_complaint import CommentComplaint
from complaints.models.group_complaint import GroupComplaint
from complaints.models.post_complaint import PostComplaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('complaint',)

    def create(self, validated_data):
        user = self.context['request'].user
        if self.Meta.model.objects.filter(user=user,
                                          **validated_data).exists():
            raise serializers.ValidationError('вы уже оставили жалобу')
        return self.Meta.model.objects.create(user=user, **validated_data)


class PostComplaintSerializer(ComplaintSerializer):
    class Meta:
        model = PostComplaint
        fields = ComplaintSerializer.Meta.fields + ('post',)


class CommentComplaintSerializer(ComplaintSerializer):
    class Meta:
        model = CommentComplaint
        fields = ComplaintSerializer.Meta.fields + ('comment',)


class GroupComplaintSerializer(ComplaintSerializer):
    class Meta:
        model = GroupComplaint
        fields = ComplaintSerializer.Meta.fields + ('group',)
