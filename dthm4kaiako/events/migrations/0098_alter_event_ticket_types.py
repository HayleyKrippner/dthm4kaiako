# Generated by Django 3.2.15 on 2022-09-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0097_auto_20220910_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ticket_types',
            field=models.ManyToManyField(blank=True, null=True, related_name='events', to='events.Ticket'),
        ),
    ]