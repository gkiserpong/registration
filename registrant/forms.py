from email.policy import default
from django import forms
from event.models import Event


class Tetot(forms.Form):
    Kentut = forms.CharField()

# member 
MEMBER_CHOICES =( 
    (1, "1"), 
    (2, "2"), 
    (3, "3"), 
    (4, "4"), 
) 

class RegisterForm(forms.Form):
    nama = forms.CharField(label="Nama Lengkap Anda")
    email = forms.EmailField(label="Alamat Email Yang Masih Valid")
    telepon = forms.CharField(label="Nomor HP")
    event = forms.ModelChoiceField(
        label="Pilih Jadwal Ibadah",
        queryset=Event.objects.filter(is_active=True),
        widget=forms.RadioSelect()
    )
    jumlah = forms.ChoiceField(
        label="Berapa yang datang? (Termasuk Anda)",
        choices=MEMBER_CHOICES,
        initial=1
    )  


class QueryQrForm(forms.Form):
    email = forms.EmailField(label="Alamat Email yang digunakan untuk mendaftar")
    event = forms.ModelChoiceField(
        label="Jadwal Ibadah yang Anda mendaftar",
        queryset=Event.objects.filter(is_active=True),
        widget=forms.RadioSelect()
    )
