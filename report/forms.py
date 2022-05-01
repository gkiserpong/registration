from django import forms
from event.models import Event

class ReportForm(forms.Form):
    event = forms.ModelChoiceField(
        label="Pilih Jadwal Ibadah",
        queryset=Event.objects.filter()
    )
