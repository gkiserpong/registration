# Generated by Django 4.0.4 on 2022-04-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_jumlah_pendaftar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='info',
            field=models.CharField(default=None, max_length=200),
        ),
    ]