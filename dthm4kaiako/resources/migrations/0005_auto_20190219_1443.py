# Generated by Django 2.1.5 on 2019-02-19 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20190219_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['-name']},
        ),
    ]
