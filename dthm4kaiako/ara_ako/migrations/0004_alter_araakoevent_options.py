# Generated by Django 3.2.12 on 2022-05-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ara_ako', '0003_alter_araakoevent_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='araakoevent',
            options={'ordering': ['-event__start']},
        ),
    ]
