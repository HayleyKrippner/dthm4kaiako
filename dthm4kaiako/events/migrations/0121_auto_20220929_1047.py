# Generated by Django 3.2.15 on 2022-09-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0120_auto_20220928_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventcsv',
            name='rejected_registrations_count',
        ),
        migrations.AddField(
            model_name='eventcsv',
            name='declined_registrations_count',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Declined')], default=1),
        ),
        migrations.AlterField(
            model_name='eventregistrationscsv',
            name='educational_entities',
            field=models.BooleanField(default=False, help_text='School and/or educational organisations participants belongs to'),
        ),
        migrations.AlterField(
            model_name='eventregistrationscsv',
            name='paid',
            field=models.BooleanField(default=False, help_text='Has participant paid?'),
        ),
        migrations.AlterField(
            model_name='eventregistrationscsv',
            name='representing',
            field=models.BooleanField(default=False, help_text='Who the participant is representing at this event'),
        ),
    ]
