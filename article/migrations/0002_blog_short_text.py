# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_text',
            field=models.TextField(default='', verbose_name='Краткое описание'),
            preserve_default=False,
        ),
    ]
