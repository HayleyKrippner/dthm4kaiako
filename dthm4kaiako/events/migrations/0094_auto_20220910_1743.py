# Generated by Django 3.2.15 on 2022-09-10 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0093_alter_eventapplicationscsv_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventapplicationscsv',
            name='dietary_requirements',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventapplicationscsv',
            name='educational_entities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventapplicationscsv',
            name='email_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventapplicationscsv',
            name='how_we_can_best_accommodate_them',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventapplicationscsv',
            name='mobile_phone_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventapplicationscsv',
            name='region',
            field=models.BooleanField(default=False),
        ),
    ]
