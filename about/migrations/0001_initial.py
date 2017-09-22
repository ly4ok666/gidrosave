# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 14:35
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('about_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name_plural': 'О компании',
                'db_table': 'about',
                'verbose_name': 'О компании',
            },
        ),
    ]