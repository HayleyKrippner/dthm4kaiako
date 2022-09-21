# Generated by Django 3.2.15 on 2022-09-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0106_auto_20220921_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='close_datetime',
            field=models.DateTimeField(blank=True, help_text='This is the date and time that participants registerations close for this event.\n\nDesired format is YYYY-MM-DD hh:mm:ss, e.g. 2022-06-09 11:30:00 (9th May 2022 at 11.30am)', null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='open_datetime',
            field=models.DateTimeField(blank=True, help_text='This is the date and time that participants can begin registering for this event.\n\nDesired format is YYYY-MM-DD hh:mm:ss, e.g. 2022-06-09 11:30:00 (9th May 2022 at 11.30am)', null=True),
        ),
    ]