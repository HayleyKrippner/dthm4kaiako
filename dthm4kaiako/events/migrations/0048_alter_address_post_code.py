# Generated by Django 3.2.13 on 2022-05-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_alter_event_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.IntegerField(default='8041', help_text='Post code, for example: 8041'),
        ),
    ]