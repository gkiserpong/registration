from .models import Registrant, Member
from rest_framework import serializers


class RegistrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registrant
        fields = ['id', 'nama', 'email', 'telepon', 'event']

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'nama', 'registrant']
