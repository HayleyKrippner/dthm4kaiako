# Generated by Django 3.2.14 on 2022-07-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0067_auto_20220720_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedEventApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deleted', models.DateTimeField(auto_now_add=True)),
                ('deletion_reason', models.PositiveSmallIntegerField(choices=[(1, 'Register to attend event'), (2, 'Apply to attend event'), (3, 'Visit event website'), (4, 'This event is invite only'), (5, 'Other')], default=1)),
                ('other_reason_for_deletion', models.DateTimeField(blank=True, default='', max_length=300, null=True)),
            ],
        ),
    ]
