from django.contrib import admin
from event.models import Event

# Event
class EventAdmin(admin.ModelAdmin):
    fields = ['nama', 'info', 'lokasi', 'tanggal', 
            'kapasitas', 'jumlah_pendaftar', 'kehadiran', 'is_active']
    
    readonly_fields=('jumlah_pendaftar', 'kehadiran', 'is_active', )
    
    list_display = ['nama', 'tanggal', 'lokasi',
            'kapasitas', 'jumlah_pendaftar', 'is_active']

admin.site.register(Event, EventAdmin)
