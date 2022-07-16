from rest_framework import viewsets
from django_crud.marketplace.models.bicycle import Bicycle
from django_crud.marketplace.serializers.bicycle import BicycleSerializer
from rest_framework import permissions


class BicycleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
    permission_classes = [permissions.IsAuthenticated]
