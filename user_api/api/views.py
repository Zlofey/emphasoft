from django.contrib.auth.models import User
from rest_framework import  permissions
from rest_framework.viewsets import ModelViewSet
from api.serializers import ReadOnlyUserSerializerSerializer, WriteOnlyUserSerializerSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ReadOnlyUserSerializerSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteOnlyUserSerializerSerializer

        elif self.request.method == 'PUT':
            return WriteOnlyUserSerializerSerializer

        elif self.request.method == 'PATCH':
            return WriteOnlyUserSerializerSerializer

        elif self.request.method == 'GET':
            return ReadOnlyUserSerializerSerializer