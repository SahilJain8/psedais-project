# Generated by Django 4.2 on 2023-07-04 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salonmanager', '0005_appointment_amount_to_be_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='discount',
        ),
    ]
