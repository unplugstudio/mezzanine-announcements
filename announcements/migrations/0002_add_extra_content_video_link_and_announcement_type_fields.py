# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-05 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='extra_content',
            field=models.TextField(blank=True, verbose_name='Extra Content (optional)'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='video_link',
            field=models.URLField(blank=True, verbose_name='Video URL'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announcement_type',
            field=models.IntegerField(choices=[(0, 'Email popup')], default=0, verbose_name='Announcement type'),
        ),
    ]
