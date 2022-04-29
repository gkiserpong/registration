from django.contrib import admin
from event.models import Event

# Event
class EventAdmin(admin.ModelAdmin):
    fields = ['nama', 'info', 'lokasi', 'tanggal', 'kapasitas', 'is_active']
    list_display = ['id', 'nama', 'tanggal', 'lokasi',
                    'kapasitas', 'jumlah_pendaftar']

admin.site.register(Event, EventAdmin)