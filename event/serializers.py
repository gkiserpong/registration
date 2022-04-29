from event.models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'nama', 'info', 'lokasi', 'tanggal',
                  'kapasitas', 'jumlah_pendaftar', 'is_active']
