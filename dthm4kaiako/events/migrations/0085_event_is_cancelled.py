# Generated by Django 3.2.15 on 2022-09-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0084_alter_event_registration_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_cancelled',
            field=models.BooleanField(default=False, help_text='This event has been cancelled'),
        ),
    ]
