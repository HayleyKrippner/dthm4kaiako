# Generated by Django 3.2.15 on 2022-09-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0111_alter_deletedeventapplication_deletion_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedeventapplication',
            name='deletion_reason',
            field=models.PositiveSmallIntegerField(choices=[(3, 'No longer interested'), (4, 'Change of plans'), (5, 'No funding'), (6, 'Inconvient location'), (7, 'Other')], default=1, help_text='Reason the participant has chosen to withdraw their application.'),
        ),
    ]