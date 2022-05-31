from django.contrib import admin
from event.models import Event

# Event
class EventAdmin(admin.ModelAdmin):
    fields = ['nama', 'info', 'lokasi', 'tanggal', 
            'kapasitas', 'jumlah_pendaftar', 'kehadiran', 'is_active']
    
    readonly_fields=('jumlah_pendaftar', 'kehadiran', 'is_active', )
    
    list_display = ['nama', 'tanggal', 'lokasi',
            'kapasitas', 'jumlah_pendaftar', 'kehadiran', 'is_active']

    def has_change_permission(self, request, obj=None):
        if obj is not None and not obj.is_active:
            return False
        return super().has_change_permission(request, obj=obj)


admin.site.register(Event, EventAdmin)
