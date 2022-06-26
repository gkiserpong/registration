from django.contrib import admin
from event.models import Event
from .models import Registrant, Member
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class RegistrantResource(resources.ModelResource):
    class Meta:
        model = Registrant
        fields = (
            'nama', 'email', 'telepon', 'wilayah__nama',
            'jumlah', 'kursi', 'is_come'
        )
        export_order = (
            'nama', 'email', 'telepon', 'wilayah__nama',
            'jumlah', 'kursi', 'is_come'
        )


class RegistrantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RegistrantResource
    fields = ['nama', 'email', 'telepon', 'wilayah', 
            'event', 'jumlah', 'kursi', 'is_come', 'is_active']
    
    readonly_fields=('nama', 'email', 'telepon', 
            'wilayah', 'event', 'jumlah', 'kursi',) # 'is_come', 'is_active', )
    
    list_display = ('nama', 'email', 'telepon', 'wilayah',
            'event', 'jumlah', 'kursi', 'is_come', 'is_active')

    list_filter = ['event__nama_event',]
    search_fields = ['nama', 'email', 'event__nama', 'event__nama_event']
    #search_fields = ('nama', 'kursi',)

#    def event_filter(obj):
#        return '%s - %s' % (obj.event.nama, obj.event.tanggal)

#class MemberAdmin(admin.ModelAdmin):
#    fields = ['nama', 'registrant']
#    fields = ('id', 'nama', 'registrant')


admin.site.register(Registrant, RegistrantAdmin)
#admin.site.register(Member, MemberAdmin)
