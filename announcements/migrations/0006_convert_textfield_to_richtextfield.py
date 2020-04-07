# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-04-06 18:41
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0005_default_start_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='content',
            field=mezzanine.core.fields.RichTextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='extra_content',
            field=mezzanine.core.fields.RichTextField(blank=True, verbose_name='Extra Content (optional)'),
        ),
    ]