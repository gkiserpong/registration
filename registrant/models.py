from django.db import models
from pkg_resources import require
from event.models import Event
from wilayah.models import Wilayah
from django.db.models.signals import post_save
from django.dispatch import receiver


# Registrant
class Registrant(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telepon = models.CharField(max_length=30)
    wilayah = models.ForeignKey(
        Wilayah,
        on_delete=models.CASCADE,
        default=18
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        limit_choices_to={'is_active': True}
    )
    jumlah = models.IntegerField(default=1)
    kursi = models.CharField(max_length=20, blank=True)
    is_come = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createt_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "registrant"
        verbose_name_plural = "Registrants"

    def __str__(self):
        return "%s" % (self.nama)

    def clean(self):
        self.email = self.email.lower()

"""
@receiver(post_save, sender=Registrant)
def auto_create_member(sender, instance, created, **kwargs):
    if created:
        first_member = Member(nama=instance.nama, registrant=instance)
        first_member.save()

@receiver(post_save, sender=Registrant)
def auto_increase_jumlah_pendaftar(sender, instance, created, **kwargs):
    if created:
        registrant = Registrant.objects.get(id=instance.id)
        event = Event.objects.get(id=registrant.event.id)
        event.jumlah_pendaftar += registrant.jumlah
        event.save()
"""

# Member
class Member(models.Model):
    nama = models.CharField(max_length=100)
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    createt_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "member"
        verbose_name_plural = "Members"

    def __str__(self):
        return "%s" % (self.nama)
