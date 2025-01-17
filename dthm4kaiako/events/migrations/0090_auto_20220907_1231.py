# Generated by Django 3.2.15 on 2022-09-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0089_auto_20220907_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventapplication',
            name='emergency_contact_first_name',
            field=models.CharField(max_length=200, verbose_name="emergency contact's first name"),
        ),
        migrations.AlterField(
            model_name='eventapplication',
            name='emergency_contact_last_name',
            field=models.CharField(default='', max_length=200, verbose_name="emergency contact's last name"),
        ),
        migrations.AlterField(
            model_name='eventapplication',
            name='emergency_contact_phone_number',
            field=models.CharField(max_length=40, verbose_name="emergency contact's phone number"),
        ),
        migrations.AlterField(
            model_name='eventapplication',
            name='emergency_contact_relationship',
            field=models.CharField(max_length=150, verbose_name='relationship with emergency contact'),
        ),
    ]
