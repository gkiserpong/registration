from django.contrib import admin
from .models import Pin


class PinAdmin(admin.ModelAdmin):
    class Meta:
        model = Pin


admin.site.register(Pin, PinAdmin)