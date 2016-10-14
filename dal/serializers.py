from rest_framework import serializers
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User


class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Permission


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group

class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ContentType