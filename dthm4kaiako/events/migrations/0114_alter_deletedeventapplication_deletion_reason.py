# Generated by Django 3.2.15 on 2022-09-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0113_alter_deletedeventapplication_deletion_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedeventapplication',
            name='deletion_reason',
            field=models.PositiveSmallIntegerField(choices=[(1, 'No longer interested'), (2, 'Change of plans'), (3, 'No funding'), (4, 'Inconvient location')], default=8, help_text='Reason the participant has chosen to withdraw their application.'),
        ),
    ]
