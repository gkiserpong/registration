# Generated by Django 4.0.4 on 2022-04-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrant', '0003_registrant_jumlah'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrant',
            name='is_come',
            field=models.BooleanField(default=False),
        ),
    ]
