from rest_framework import serializers
from user_resource.models import PlayerUser, ManagerUser

class PlayerUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerUser
        fields = ['id', 'password_hash', 'firstname', 'lastname', 'manager']
    

class ManagerUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManagerUser
        fields = ['id', 'password_hash', 'firstname', 'lastname']
