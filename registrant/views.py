from urllib import request
from django.shortcuts import render
from django.conf import settings 

from registrant.models import Registrant
from .forms import RegisterForm, QueryQrForm
from event.models import Event
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def qr_scan(request):
    if request.POST:
        registrantid = request.POST.get('id', None)
        #registrantid = context['id']
        registrant = Registrant.objects.get(id=registrantid)
        event = Event.objects.get(id=registrant.event.id)

        registrant.is_come = True
        registrant.save()

        event_context = {
            'nama' : registrant.nama,
            'email' : registrant.email,
            'telepon' : registrant.telepon,
            'jumlah': registrant.jumlah,
            'event_id': registrant.event,
            'event_nama' : event.nama,
            'event_info' : event.info,
            'event_lokasi' : event.lokasi,
            'event_tanggal' : event.tanggal,
            'event_kapasitas' : event.kapasitas,
        }

        return render(request, "qr_scan.html", event_context)

    return HttpResponseNotFound("404")

#qr_scanned
def qr_check(request):

    registrantid = request.GET.get('id', None)
    registrant = Registrant.objects.get(id=registrantid)
    event = Event.objects.get(id=registrant.event.id)

    event_context = {
        'nama' : registrant.nama,
        'email' : registrant.email,
        'telepon' : registrant.telepon,
        'jumlah': registrant.jumlah,
        'event_id': registrant.event,
        'event_nama' : event.nama,
        'event_info' : event.info,
        'event_lokasi' : event.lokasi,
        'event_tanggal' : event.tanggal,
        'event_kapasitas' : event.kapasitas,
    }

    return render(request, "qr_check.html", event_context)
    

#qr_ok
def qr_ok(request):
    if request.POST:
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        telepon = request.POST.get('telepon')
        jumlah = request.POST.get('jumlah')
        eventid = request.POST.get('event')

        email_used = Registrant.objects.filter(
            email=email,
            is_come=False
        )
    
        if email_used:
            return render(request, "email_used.html", {"email": email})

        event = Event.objects.get(id=eventid)
        reg = Registrant.objects.create(
            nama = nama,
            email = email,
            telepon = telepon,
            event = event,
        )

        
        context = {
            'id' : reg.id,
            'nama': nama,
            'email': email,
            'telepon': telepon,
            'event': eventid,
            'jumlah': jumlah,
        }
        return render(request, "qr_ok.html", context)

    return HttpResponseNotFound("404")
    

# out_capacity
def out_capacity(request,context):
    return render(request, "out_capacity.html", context)


# confirmation_request
def confirmation_request(request, context):

    event = Event.objects.get(id=context['event'])

    kapasitas_sekarang = event.kapasitas - event.jumlah_pendaftar

    event_context = {
        'nama' : context['nama'],
        'email' : context['email'],
        'telepon' : context['telepon'],
        'jumlah': context['jumlah'],
        'event_id': context['event'],
        'event_nama' : event.nama,
        'event_info' : event.info,
        'event_lokasi' : event.lokasi,
        'event_tanggal' : event.tanggal,
        'event_kapasitas' : event.kapasitas,
        'kapasitas' : kapasitas_sekarang,
        'base_url': settings.BASE_URL
    }

    email_used = Registrant.objects.filter(
            email=context['email'],
            is_come=False
        )
    
    if email_used:
        return render(request, "email_used.html", event_context)

    if kapasitas_sekarang < int(context['jumlah']):
        return out_capacity(request, event_context)

    return render(request, "confirmation.html", event_context)

#register_request
def register_request(request):
    if request.method == 'POST':
        #form_register = RegisterForm(request.POST)
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            telepon = form.cleaned_data['telepon']
            jumlah = form.cleaned_data['jumlah']
            eventid = request.POST.get('event')
            
            context = {
                'nama': nama,
                'email': email,
                'telepon': telepon,
                'event': eventid,
                'jumlah': jumlah,

            }
            return confirmation_request(request, context)
    else:
        form = RegisterForm()
        
    
    return render(request, "register_form.html", {"form": form})


def query_qr(request):
    if request.method == 'POST':
        form = QueryQrForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            eventid = request.POST.get('event')

            try:
                registrant = Registrant.objects.get(
                    email = email,
                    event = eventid,
                    is_come = False
                )

                event = Event.objects.get(id=registrant.event.id)

                event_context = {
                    'id' : registrant.id,
                    'nama' : registrant.nama,
                    'email' : registrant.email,
                    'telepon' : registrant.telepon,
                    'jumlah': registrant.jumlah,
                    'event_id': registrant.event,
                    'event_nama' : event.nama,
                    'event_info' : event.info,
                    'event_lokasi' : event.lokasi,
                    'event_tanggal' : event.tanggal,
                    'event_kapasitas' : event.kapasitas,
                }

                return render(request, "qr_check.html", event_context)
            
            except:
                return HttpResponseNotFound("404")
        
    else:
        form = QueryQrForm()

    return render(request, "query_qr.html", {'form': form})