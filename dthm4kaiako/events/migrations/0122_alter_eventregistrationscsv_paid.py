# Generated by Django 3.2.15 on 2022-09-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0121_auto_20220929_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistrationscsv',
            name='paid',
            field=models.BooleanField(default=False, help_text='Has the participant paid?'),
        ),
    ]
