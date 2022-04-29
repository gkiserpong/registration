# Generated by Django 4.0.4 on 2022-04-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('lokasi', models.CharField(default='GKI Serpong', max_length=100)),
                ('tanggal', models.DateTimeField()),
                ('kapasitas', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('createt_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'db_table': 'event',
            },
        ),
    ]
