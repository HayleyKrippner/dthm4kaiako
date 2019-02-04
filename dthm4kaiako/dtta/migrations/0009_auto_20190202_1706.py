# Generated by Django 2.1.5 on 2019-02-02 04:06

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import utils.get_upload_filepath


class Migration(migrations.Migration):

    dependencies = [
        ('dtta', '0008_auto_20190129_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticleAudience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('colour', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticleSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=utils.get_upload_filepath.get_dtta_news_article_source_upload_path)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='audiences',
            field=models.ManyToManyField(blank=True, related_name='news_articles', to='dtta.NewsArticleAudience'),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_articles', to='dtta.NewsArticleSource'),
        ),
    ]
