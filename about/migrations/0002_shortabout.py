# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_text', models.TextField(verbose_name='Краткое описание')),
                ('short_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.About')),
            ],
            options={
                'db_table': 'shortabout',
            },
        ),
    ]