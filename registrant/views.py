from urllib import request
from django.shortcuts import render
from django.conf import settings 

from registrant.models import Registrant
from .forms import RegisterForm, QueryQrForm
from event.models import Event
from wilayah.models import Wilayah
from django.http import HttpResponseNotFound
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags


#qr_query
def qr_check(request):

    registrantid = request.GET.get('id', None)
    registrant = Registrant.objects.get(id=registrantid)
    event = Event.objects.get(id=registrant.event.id)

    event_context = {
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
        wilayahid = request.POST.get('wilayah')

        email_used = Registrant.objects.filter(
            email=email,
            is_come=False,
            is_active=True
        )
    
        if email_used:
            return render(request, "email_used.html", {"email": email})

        event = Event.objects.get(id=eventid)
        wilayah = Wilayah.objects.get(id=wilayahid)
    
        reg = Registrant.objects.create(
            nama = nama,
            email = email,
            telepon = telepon,
            event = event,
            jumlah = jumlah,
            wilayah = wilayah,
        )
        
        context = {
            'id' : reg.id,
            'nama': nama,
            'email': email,
            'telepon': telepon,
            'jumlah': jumlah,
            'wilayah': wilayah.id,
            'wilayah_nama': wilayah.nama,
            #'event': eventid,
            'event': event.id,
            'event_nama': event.nama,
            'event_info': event.info,
            'event_tanggal': event.tanggal,
            'event_lokasi': event.lokasi,
            'base_url': settings.BASE_URL
        }

        # Sending Email
        subject = '[QRCode] ' + event.nama + ' - ' + nama
        html_message = render_to_string('qr_ok_email.html', context)
        from_email = settings.EMAIL_HOST_USER 
        to_email = reg.email

        message = EmailMessage(subject, html_message, from_email, [to_email])
        message.content_subtype = 'html' # this is required because there is no plain text email message
        
        try:
            message.send()
        except:
            pass

        return render(request, "qr_ok.html", context)

    return HttpResponseNotFound("404")
    

# out_capacity
def out_capacity(request,context):
    return render(request, "out_capacity.html", context)


# confirmation_request
def confirmation_request(request, context):

    event = Event.objects.get(id=context['event'])
    wilayah = Wilayah.objects.get(id=context['wilayah'])

    kapasitas_sekarang = event.kapasitas - event.jumlah_pendaftar

    event_context = {
        'nama' : context['nama'],
        'email' : context['email'],
        'telepon' : context['telepon'],
        'jumlah': context['jumlah'],
        'wilayah_id': wilayah.id,
        'wilayah_nama': wilayah.nama,
        'event_id': event.id,
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
            is_come=False,
            is_active=True
        )
    
    if email_used:
        # Email is used for register
        error_context = {
            "title" : "Maaf, Email Sudah Terpakai",
            "message" : "Email <strong>" 
                + str(context['email']) 
                + "</strong> sudah terpakai. Mohon menggunakan email yang lain."
        } 
        #return render(request, "email_used.html", event_context)
        return render(request, "error.html", error_context)

    if kapasitas_sekarang < int(context['jumlah']):
        error_context = {
            "title" : "Maaf, Kapasitas tidak cukup",
            "message" : "Anda mendaftar untuk <strong>" 
                + str(context['jumlah']) + "</strong> orang. Kapasitas hanya <strong>" 
                + str(kapasitas_sekarang) + "</strong> orang."
        }
        return render(request, "error.html", error_context)
        #return render(request, "out_capacity.html", event_context)

    return render(request, "confirmation.html", event_context)

#register_request
def register_request(request):
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            telepon = form.cleaned_data['telepon']
            jumlah = form.cleaned_data['jumlah']
            eventid = request.POST.get('event')
            wilayahid = request.POST.get('wilayah')
            
            context = {
                'nama': nama,
                'email': email,
                'telepon': telepon,
                'event': eventid,
                'jumlah': jumlah,
                'wilayah': wilayahid,
            }
            
            return confirmation_request(request, context)

    else:
        event = Event.objects.filter(is_active=True)
        if event:
            form = RegisterForm()
        else:
            error_context = {
                "title" : "Maaf, Tidak ada Ibadah Onsite",
                "message" : "Saat ini, kami tidak menemukan data Ibadah Onsite di database."
            }   
            return render(request, "error.html", error_context) 
            #return render(request, "no_event.html")

    return render(request, "register_form.html", {"form": form})


def qr_query(request):
    if request.method == 'POST':
        
        form = QueryQrForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            eventid = request.POST.get('event')

            try:
                registrant = Registrant.objects.get(
                    email = email,
                    event = eventid,
                    is_active = True
                )
                is_found = True
            except:
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
                }

                return render(request, "qr_check.html", event_context)
            
            else:
                # QR is not found
                error_context = {
                    "title" : "Maaf, Data tidak ditemukan",
                    "message" : "Data untuk email <strong>" + email + "</strong> ini tidak di temukan."
                }
                #return render(request, "qr_not_found.html", {'email': email})
                return render(request, "error.html", error_context)
        
    else:
        event = Event.objects.filter(is_active=True)
        if event:
            form = QueryQrForm()
            return render(request, "qr_query.html", {"form": form})

    # No Event
    error_context = {
        "title" : "Maaf, Tidak ada Ibadah Onsite",
        "message" : "Saat ini, kami tidak menemukan data Ibadah Onsite di database."
    }   
    return render(request, "error.html", error_context) 
    #return render(request, "no_event.html")


def qr_cancel(request):

    if request.POST:
        try:
            registrant = Registrant.objects.get(id=request.POST.get('id'))
            is_found = True

        except:
            is_found = False

        if is_found:
            event = Event.objects.get(id=registrant.event.id)
            event.jumlah_pendaftar -= registrant.jumlah
            event.save()

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
            }

            registrant.delete()

            return render(request, "qr_cancel.html", event_context)
        
        else:
            # Not Found Registrant
            error_context = {
                "title" : "Maaf, Data tidak ditemukan",
                "message" : "Data tidak di temukan di database kami."
            }
            return render(request, "error.html", error_context)
            #return render(request, "not_found.html")

    return HttpResponseNotFound("404")
