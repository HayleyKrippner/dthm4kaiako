# Generated by Django 3.2.14 on 2022-07-30 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0076_auto_20220730_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='staff',
            new_name='event_staff',
        ),
    ]
