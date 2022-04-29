from rest_framework import viewsets
#from rest_framework import permissions
from .serializers import RegistrantSerializer, MemberSerializer
from .models import Registrant, Member


class RegistrantApiSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registrant to be viewed or edited.
    """
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
    #permission_classes = [permissions.IsAuthenticated]

class MemberApiSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registrant to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    #permission_classes = [permissions.IsAuthenticated]
