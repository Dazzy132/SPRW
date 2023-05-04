from rest_framework import serializers
from complaints.models.comment_complaint import CommentComplaint
from complaints.models.group_complaint import GroupComplaint
from complaints.models.post_complaint import PostComplaint
from complaints.models.profile_complaint import ProfileComplaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('complaint',)

    def create(self, validated_data):
        user = self.context['request'].user
        if self.Meta.model.objects.filter(user=user,
                                          **validated_data).exists():
            raise serializers.ValidationError(
                {'error': 'Вы уже оставили жалобу'})
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


class ProfileComplaintSerializer(ComplaintSerializer):
    class Meta:
        model = ProfileComplaint
        fields = ComplaintSerializer.Meta.fields + ('profile',)

    def validate_profile(self, profile):
        if profile.user == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете оставить жалобу на самого себя')
        return profile
