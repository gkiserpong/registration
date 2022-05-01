from .models import Event
from registrant.models import Registrant
from django.utils.timezone import now, timedelta

def check_event_expiry():

    closetime = now() - timedelta(minutes=30)
    event = Event.objects.filter(
        tanggal__lt = closetime,
        is_active = True
    )

    if event:
        for ev in event:
            registrant = Registrant.objects.filter(event=ev.id)
            if registrant:
                for reg in registrant:
                    reg.is_active = False
                    reg.save()
                
            ev.is_active = False
            ev.save()


