from django.db import models


class Pin(models.Model):
    pin = models.CharField(max_length=6, default='778899')