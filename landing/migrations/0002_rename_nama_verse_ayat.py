# Generated by Django 3.2.12 on 2022-05-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verse',
            old_name='nama',
            new_name='ayat',
        ),
    ]
