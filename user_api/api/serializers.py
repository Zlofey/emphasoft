from rest_framework import serializers
from django.contrib.auth.models import User


class WriteOnlyUserSerializerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'is_active',
        ]
        extra_kwargs = {
            'username': {'required': True},
            'is_active': {'required': True},
            'password': {'required': True}
        }


class ReadOnlyUserSerializerSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'last_login',
            'is_superuser',
        ]
        read_only_fields = ['id', 'last_login', 'is_superuser']
        extra_kwargs = {
            'username': {'required': True},
            'is_active': {'required': True}
        }


