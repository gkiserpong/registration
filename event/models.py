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
    jumlah_pendaftar = models.IntegerField(default=0)
    kehadiran = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    createt_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "event"
        verbose_name_plural = "Events"

    def __str__(self):
        tanggal = timezone.localtime(self.tanggal)
        return "%s - %s, %s - Kapasitas: %s" % (
            self.nama, 
            _(tanggal.strftime('%A')),
            _(tanggal.strftime('%H:%M %d/%m/%Y')),
            (self.kapasitas - self.jumlah_pendaftar))
        #return "%s (%s)" % (self.nama, (self.kapasitas-self.jumlah_pendaftar))

    def clean(self):
        if self.tanggal < now():
            raise ValidationError(_("Tanggal tidak bisa di masa lalu!"))
        if self.kapasitas < 0:
            raise ValidationError(_("Kapasitas tidak tidak boleh negatif!"))
        