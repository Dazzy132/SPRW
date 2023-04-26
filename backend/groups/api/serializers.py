from rest_framework import serializers

from posts.api.serializers import PostGETSerializer
from groups.models import Groups



class GroupsSerializer(serializers.ModelSerializer):
    posts = PostGETSerializer(many=True, required=False)

    class Meta:
        model = Groups
        fields = ('name', 'group_slug', 'group_creator', 'group_moderator', 'posts',
                  'image', 'is_closed_group', 'subscribers')




    


