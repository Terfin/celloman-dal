from rest_framework import serializers
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import Client

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User



class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group

class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType


class ClientSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateField(source='joined_date', read_only=True)

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'username', 'address', 'contact_number', 'id', 'calls_to_center', 'date_joined')