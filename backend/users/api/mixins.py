from rest_framework.mixins import (DestroyModelMixin,
                                   ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class PatchModelMixin(object):
    def partial_update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ListRetrieveUpdateDestroyViewSet(ListModelMixin, PatchModelMixin,
                                       RetrieveModelMixin, DestroyModelMixin,
                                       GenericViewSet):
    pass
