# Generated by Django 3.2.14 on 2022-07-31 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0078_alter_eventapplication_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventapplication',
            name='reason_for_withdrawing',
        ),
    ]
