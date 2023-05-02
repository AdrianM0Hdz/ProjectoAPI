from rest_framework import serializers
from user_resource.models import (
    PlayerUser, 
    ManagerUser, 
    PartidaFallingObjects, 
    PartidaEncontrarDiferencias 
)

class PlayerUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerUser
        fields = ['id', 'password_hash', 'firstname', 'lastname', 'manager']
    

class ManagerUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManagerUser
        fields = ['id', 'password_hash', 'firstname', 'lastname']

class PartidaFallingObjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartidaFallingObjects
        fields = ['id', 'player', 'score', 'time']

class PartidaEncontrarDiferenciasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartidaEncontrarDiferencias
        fields = ['id', 'player', 'maxtime', 'n_objects', 'time', 'found_objects']