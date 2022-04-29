from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event to be viewed or edited.
    """
    #queryset = Event.objects.get(is_active=True)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [permissions.IsAuthenticated]
