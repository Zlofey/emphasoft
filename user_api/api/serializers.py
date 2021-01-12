from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'is_active',
        ]
        extra_kwargs = {
            'username': {'required': True},
            'is_active': {'required': True},
            'password': {'required': True, 'write_only': True},
            'id': {'required': False, 'read_only': True}
        }

    def create(self, validated_data, partial=True):
        user = User(
            username=validated_data['username'],
            is_active=validated_data['is_active'],

            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data, partial=True):
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance

