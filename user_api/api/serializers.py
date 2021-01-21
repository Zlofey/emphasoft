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

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if instance and 'password' in self.validated_data:
            instance.set_password(self.validated_data['password'])
            instance.save()
            self.validated_data['password'] = instance.password
        return instance
#testing git
