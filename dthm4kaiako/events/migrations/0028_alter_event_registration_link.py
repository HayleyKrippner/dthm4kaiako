# Generated by Django 3.2.12 on 2022-05-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_auto_20220503_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]