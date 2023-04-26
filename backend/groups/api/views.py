
from groups.api.serializers import GroupsSerializer
from rest_framework.viewsets import ModelViewSet

from groups.models import Groups


class GroupViewSet(ModelViewSet):
    serializer_class = GroupsSerializer
    queryset = Groups.objects.all()
    lookup_field = 'group_slug'

