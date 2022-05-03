from django.contrib import admin
from event.models import Event
from .models import Registrant, Member


class RegistrantAdmin(admin.ModelAdmin):
    fields = ['nama', 'email', 'telepon', 'wilayah', 
            'event', 'jumlah', 'kursi', 'is_come', 'is_active']
    
    readonly_fields=('nama', 'email', 'telepon', 
            'wilayah', 'event', 'jumlah', 'kursi', 'is_come', 'is_active', )
    
    list_display = ('id', 'nama', 'email', 'telepon', 'wilayah', 
            'event', 'jumlah', 'kursi', 'is_come', 'is_active')
    
    list_filter = ('nama', 'kursi',)

#class MemberAdmin(admin.ModelAdmin):
#    fields = ['nama', 'registrant']
#    fields = ('id', 'nama', 'registrant')


admin.site.register(Registrant, RegistrantAdmin)
#admin.site.register(Member, MemberAdmin)
