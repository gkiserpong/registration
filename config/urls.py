from django.contrib import admin
from django.urls import path, include
from registrant.views import register_request, qr_check, qr_ok, qr_query, qr_cancel
from qrscan.views import qr_scan, pin_entry
from landing.views import landing

#from rest_framework import routers
#from event.apis import EventViewSet
#from registrant.apis import RegistrantApiSet, MemberApiSet

#router = routers.DefaultRouter()
#router.register(r'event', EventViewSet)
#router.register(r'registrant', RegistrantApiSet)
#router.register(r'member', MemberApiSet)

urlpatterns = [
    path('', landing, name="landing"),
    path('admin/', admin.site.urls),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', register_request, name="register"),
    path('qr_ok', qr_ok, name="qr_ok"),
    path('qr_check', qr_check, name="qr_check"),
    path('qr_scan', qr_scan, name="qr_scan"),
    path('cancel', qr_cancel, name="cancel"),
    path('query', qr_query, name="query"),
    path('pin', pin_entry, name="pin"),
]
