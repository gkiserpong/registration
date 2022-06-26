from multiprocessing import Event
from django.shortcuts import render

from registrant.models import Registrant
from .forms import ReportForm
from event.models import Event


# Create your views here.
def report(request):
    
    if request.POST:
        form = ReportForm(request.POST)

        if form.is_valid:
            event = Event.objects.get(id=request.POST.get('event'))
            registrant = Registrant.objects.filter(event=request.POST.get('event'))
            email_count = Registrant.objects.count(event=request.POST.get('event'))
            context = {
                'event': event,
                'registrant': registrant,
                'form': form,
                'email_count': email_count,
            }
            return render(request, "report_form.html", context)
        else:
            context = {}

        return render(request, "report_form.html", {'form': form})

    else:
        form = ReportForm()
    
    return render(request, "report_form.html", {'form': form})