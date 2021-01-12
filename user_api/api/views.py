from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from api.serializers import UserSerializer
from api.permissions import IsSelfOrAdmin, ReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # only super user can create
        if self.action == 'create':
            return [permissions.IsAdminUser()]

        # super user or owner of profile can destroy   update   partial_update
        if self.action in ('destroy', 'update', 'partial_update'):
            return [IsSelfOrAdmin()]

        return [ReadOnly()]
