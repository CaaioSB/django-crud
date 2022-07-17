from rest_framework import viewsets
from rest_framework.response import Response

from django_crud.marketplace.models.bicycle import Bicycle
from django_crud.marketplace.serializers.bicycle import BicycleSerializer
from rest_framework import permissions
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet


class BicycleViewSet(GenericViewSet,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     ListModelMixin):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)

        return Response(serializer.data)
