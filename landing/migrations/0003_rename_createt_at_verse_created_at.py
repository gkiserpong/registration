# Generated by Django 3.2.12 on 2022-05-01 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_rename_nama_verse_ayat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verse',
            old_name='createt_at',
            new_name='created_at',
        ),
    ]
