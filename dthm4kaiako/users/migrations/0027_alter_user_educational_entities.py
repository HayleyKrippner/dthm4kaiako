# Generated by Django 3.2.14 on 2022-07-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_user_educational_entities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='educational_entities',
            field=models.ManyToManyField(max_length=200, related_name='users', to='users.Entity', verbose_name='School(s) and/or educational organisation or association participiant is from'),
        ),
    ]
