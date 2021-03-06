# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 01:32
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст статьи')),
                ('article_date', models.DateTimeField(verbose_name='Дата и время')),
                ('goals_1', models.TextField(blank=True, null=True, verbose_name='Цели 1')),
                ('goals_2', models.TextField(blank=True, null=True, verbose_name='Цели 2')),
                ('article_likes', models.IntegerField(default=0)),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'статьи',
                'ordering': ['-article_date'],
                'verbose_name_plural': 'статьи',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_text', models.TextField()),
                ('features_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Article')),
            ],
            options={
                'db_table': 'features',
            },
        ),
    ]
