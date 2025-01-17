# Generated by Django 3.2.15 on 2022-09-27 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0118_alter_event_registration_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='ticket_types',
        ),
        migrations.CreateModel(
            name='ParticipantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Participant type e.g. teacher, event staff', max_length=200)),
                ('price', models.FloatField(help_text='Cost for participant type to attend in NZD')),
            ],
            options={
                'verbose_name_plural': 'participant type',
                'ordering': ['name'],
                'unique_together': {('name', 'price')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='participant_types',
            field=models.ManyToManyField(blank=True, help_text='The participant types that will be available for event participants to choose from.', related_name='events', to='events.ParticipantType'),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='participant_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_registrations', to='events.participanttype'),
        ),
        migrations.DeleteModel(
            name='TicketType',
        ),
    ]
