# Generated by Django 3.2 on 2021-12-06 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_bookinginfo_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationinfo',
            old_name='check_in',
            new_name='checkin',
        ),
        migrations.RenameField(
            model_name='reservationinfo',
            old_name='check_out',
            new_name='checkout',
        ),
    ]