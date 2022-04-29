from django.contrib import admin
from event.models import Event
from .models import Registrant, Member


class RegistrantAdmin(admin.ModelAdmin):
    fields = ['nama', 'email', 'telepon', 'event', 'jumlah', 'is_come']
    list_display = ('id', 'nama', 'email', 'telepon', 'event', 'jumlah', 'is_come')


class MemberAdmin(admin.ModelAdmin):
    fields = ['nama', 'registrant']
    fields = ('id', 'nama', 'registrant')


admin.site.register(Registrant, RegistrantAdmin)
#admin.site.register(Member, MemberAdmin)
