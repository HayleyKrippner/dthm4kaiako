# Generated by Django 3.2.14 on 2022-08-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0081_alter_eventapplication_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventapplication',
            name='admin_billing_comments',
            field=models.TextField(blank=True),
        ),
    ]
