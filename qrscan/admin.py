from django.contrib import admin
from .models import Pin


class PinAdmin(admin.ModelAdmin):
    class Meta:
        model = Pin

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Pin, PinAdmin)