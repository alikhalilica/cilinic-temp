# Generated by Django 3.1.5 on 2021-01-25 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210121_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='checked',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_type',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='updated_date',
        ),
    ]
