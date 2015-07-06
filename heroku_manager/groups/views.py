from django.shortcuts import render

from rest_framework import viewsets
from .serializers import GroupSerializer, AppSerializer
from .models import Group, App

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
