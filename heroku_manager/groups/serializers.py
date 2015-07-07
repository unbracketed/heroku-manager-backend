from rest_framework import serializers

from .models import Group, App


class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    apps = AppSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
