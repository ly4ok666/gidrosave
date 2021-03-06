# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_blog_short_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/blog/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'db_table': 'blog_images',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blogimages',
            name='article',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Blog'),
        ),
    ]
