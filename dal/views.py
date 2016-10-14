from rest_framework import viewsets
from . import serializers, permissions
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from rest_framework import permissions as builtin_perms


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (builtin_perms.IsAdminUser, permissions.IsLoggedUser)


class PermissionViewSet(viewsets.ModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    permission_classes = (builtin_perms.IsAdminUser, permissions.IsLoggedUser)


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (builtin_perms.IsAdminUser, permissions.IsLoggedUser)

class ContentTypeViewSet(viewsets.ModelViewSet):

    queryset = ContentType.objects.all()
    serializer_class = serializers.ContentTypeSerializer
    permission_classes = (builtin_perms.IsAdminUser, permissions.IsLoggedUser)
