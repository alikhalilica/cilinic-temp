# Generated by Django 2.2.17 on 2021-02-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0007_patient_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]