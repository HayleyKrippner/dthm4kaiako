# Generated by Django 3.2.12 on 2022-04-19 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_applicanttype_eventapplication_registrationform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='end_datetime',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='open_datetime',
            new_name='open',
        ),
    ]
