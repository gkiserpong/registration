from datetime import timedelta
from urllib import request
from django.shortcuts import render, redirect
from django.conf import settings 
from .forms import PinForm
from registrant.models import Registrant
from event.models import Event
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now


@csrf_exempt
def qr_scan(request):
    if request.POST:
        registrantid = request.POST.get('id', None)
        force_checkin = request.POST.get('force_checkin', None)
        
        try:
            registrant = Registrant.objects.get(id=registrantid)
            is_found = True
        except ObjectDoesNotExist:
            is_found = False
        
        if is_found:
            event = Event.objects.get(id=registrant.event.id)

            event_context = {
                'id' : registrant.id,
                'nama' : registrant.nama,
                'email' : registrant.email,
                'telepon' : registrant.telepon,
                'jumlah': registrant.jumlah,
                'wilayah_nama': registrant.wilayah,
                'event_id': registrant.event,
                'event_nama' : event.nama,
                'event_info' : event.info,
                'event_lokasi' : event.lokasi,
                'event_tanggal' : event.tanggal,
                'event_kapasitas' : event.kapasitas,
                'qr_used_at': registrant.updated_at,
            }

            # Check if now() close to event time

            event_start = event.tanggal - timedelta(hours=1)
            event_end = event.tanggal + timedelta(hours=2)

            if ((now() > event_start) and (now() < event_end)) or force_checkin:

                if registrant.is_active and not registrant.is_come:

                    registrant.is_come = True
                    registrant.is_active = False
                    registrant.save()

                    template_to_use = "qr_scan.html"
                
                else:
                    template_to_use = "qr_used.html"

            else:
                template_to_use = "event_not_start.html"

            return render(request, template_to_use, event_context)


        else:
            return render(request, "qr_not_found.html")

    return HttpResponseNotFound("404")


def pin_entry(request):
    PIN = "778899"
    if request.POST:
        form = PinForm(request.POST)

        if form.is_valid():
            pin = form.cleaned_data['pin']

            if pin == PIN:
                scanner_uri = static('qrscan/scanner/index.html')
                return render(request, "scanner.html")

    form = PinForm()

    return render(request, "pin_entry.html", {'form': form})