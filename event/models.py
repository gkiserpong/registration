from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
# Event
class Event(models.Model):
    nama = models.CharField(max_length=100)
    info = models.CharField(max_length=200, default=None)
    lokasi = models.CharField(max_length=100, default="GKI Serpong")
    tanggal = models.DateTimeField()
    kapasitas = models.IntegerField()
    blok_kursi = models.CharField(max_length=100, blank=True)
    jumlah_pendaftar = models.IntegerField(default=0)
    kehadiran = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_full_capacity = models.BooleanField(default=False)
    nama_event = models.CharField(max_length=100, blank=True)
    createt_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "event"
        verbose_name_plural = "Events"

    def __str__(self):
        tanggal = timezone.localtime(self.tanggal)
        sisa_kapasitas = self.kapasitas - self.jumlah_pendaftar
        sisa_kapasitas = sisa_kapasitas if sisa_kapasitas > 0 else 0
        return "%s - %s, %s - Sisa Kuota: %s" % (
            self.nama, 
            _(tanggal.strftime('%A')),
            _(tanggal.strftime('%H:%M %d/%m/%Y')),
            (sisa_kapasitas))

    def clean(self):
        if self.tanggal < now():
            raise ValidationError({'tanggal': _("Tanggal tidak bisa di masa lalu!")})
        if self.kapasitas < 0:
            raise ValidationError({'kapasita': _("Kapasitas tidak tidak boleh negatif!")})
        if self.kapasitas < self.jumlah_pendaftar:
            raise ValidationError({'kapasitas': _("Kapasitas tidak boleh lebih kecil dari Jumlah Pendaftar")})

    def save(self, *args, **kwargs):
        tanggal = timezone.localtime(self.tanggal)
        self.nama_event = '%s - %s, %s' % (
            self.nama,
            _(tanggal.strftime('%A')), _(tanggal.strftime('%H:%M %d/%m/%Y'))
        )
        if self.jumlah_pendaftar >= self.kapasitas and not self.is_full_capacity:
            self.is_full_capacity = True

        return super(Event, self).save(*args, **kwargs)