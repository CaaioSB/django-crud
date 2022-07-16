from rest_framework import serializers
from django_crud.marketplace.models.bicycle import Bicycle


class BicycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bicycle
        fields = ('url', 'name', 'description', 'price', 'image', 'type', 'handlebar', 'marches', 'material', 'cube', 'rear_cube', 'tires')
        read_only_fields = ('url',)
        extra_kwargs = {
            'image': {'required': False},
        }
