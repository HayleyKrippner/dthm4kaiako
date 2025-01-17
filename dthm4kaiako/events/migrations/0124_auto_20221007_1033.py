# Generated by Django 3.2.15 on 2022-10-06 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0123_event_capcity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='capcity',
        ),
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(default=1, help_text='What is the maximum number of people who can attend this event?', null=True),
        ),
    ]
