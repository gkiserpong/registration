# Generated by Django 3.2.12 on 2022-06-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_is_full_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='nama_event',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
