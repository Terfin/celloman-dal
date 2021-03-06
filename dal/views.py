from rest_framework import viewsets, permissions, filters
from . import serializers
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import Client, ClientType


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    @list_route()
    def current(self, request):
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)


class PermissionViewSet(viewsets.ModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer



class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):

    queryset = ContentType.objects.all()
    serializer_class = serializers.ContentTypeSerializer

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_fields = ('username', )

class ClientTypeViewSet(viewsets.ModelViewSet):

    queryset = ClientType.objects.all()
    serializer_class = serializers.ClientTypeSerializer