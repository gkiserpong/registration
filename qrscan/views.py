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


@csrf_exempt
def qr_scan(request):
    if request.POST:
        registrantid = request.POST.get('id', None)
        
        try:
            registrant = Registrant.objects.get(id=registrantid)
            event = Event.objects.get(id=registrant.event.id)

            event_context = {
                'nama' : registrant.nama,
                'email' : registrant.email,
                'telepon' : registrant.telepon,
                'jumlah': registrant.jumlah,
                'wilayah_name': registrant.wilayah,
                'event_id': registrant.event,
                'event_nama' : event.nama,
                'event_info' : event.info,
                'event_lokasi' : event.lokasi,
                'event_tanggal' : event.tanggal,
                'event_kapasitas' : event.kapasitas,
            }

            if registrant.is_active == True:

                registrant.is_come = True
                registrant.is_active = False
                print(registrant.is_come)
                print(registrant.is_active)
                registrant.save()

                return render(request, "qr_scan.html", event_context)
            
            else:
                return render(request, "qr_used.html", event_context)


        except ObjectDoesNotExist:
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