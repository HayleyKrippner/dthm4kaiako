# Generated by Django 3.2.12 on 2022-04-06 03:20

from django.db import migrations
from django.contrib.postgres.operations import (
    TrigramExtension,
    UnaccentExtension,
)


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20220406_1005'),
    ]

    operations = [
        TrigramExtension(),
        UnaccentExtension(),
    ]
