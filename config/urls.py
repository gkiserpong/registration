from django.contrib import admin
from django.urls import path, include
from registrant.views import register_request, qr_check, qr_scan, qr_ok, query_qr
#from rest_framework import routers
#from event.apis import EventViewSet
#from registrant.apis import RegistrantApiSet, MemberApiSet

#router = routers.DefaultRouter()
#router.register(r'event', EventViewSet)
#router.register(r'registrant', RegistrantApiSet)
#router.register(r'member', MemberApiSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', register_request, name="register"),
    path('qr_ok', qr_ok, name="qr_ok"),
    path('qr_check', qr_check, name="qr_check"),
    path('qr_scan', qr_scan, name="qr_scan"),
    path('query', query_qr, name="query_qr"),
]
