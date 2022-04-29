from email.policy import default
from operator import length_hint
from django import forms
from event.models import Event


class PinForm(forms.Form):

    pin = forms.CharField(
        widget=forms.PasswordInput(),
        label="Masukkan PIN",
        max_length=6
    )