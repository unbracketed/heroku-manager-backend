from rest_framework import serializers

from .models import Group, App


class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
