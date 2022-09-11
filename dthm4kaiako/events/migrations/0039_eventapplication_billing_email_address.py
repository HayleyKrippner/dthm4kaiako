# Generated by Django 3.2.13 on 2022-05-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_alter_eventapplication_billing_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventapplication',
            name='billing_email_address',
            field=models.CharField(default='', help_text='Email address of the person paying for your ticket', max_length=100),
        ),
    ]