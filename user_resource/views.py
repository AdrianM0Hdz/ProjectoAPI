from rest_framework import viewsets, permissions
from user_resource.serializers import ManagerUserSerializer, PlayerUserSerializer
from user_resource.models import ManagerUser, PlayerUser

# Create your views here.

class ManagerUserViewSet(viewsets.ModelViewSet):
    queryset = ManagerUser.objects.all()
    serializer_class = ManagerUserSerializer
    permission_classes = []

class PlayerUserViewSet(viewsets.ModelViewSet):
    queryset = PlayerUser.objects.all()
    serializer_class = PlayerUserSerializer
    permission_classes = []
