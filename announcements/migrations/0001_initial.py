# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_emailfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created', db_index=True)),
                ('date_start', models.DateTimeField(verbose_name='Start date', db_index=True)),
                ('date_end', models.DateTimeField(db_index=True, null=True, verbose_name='End date', blank=True)),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image', blank=True)),
                ('can_dismiss', models.BooleanField(default=True, help_text='The user can dismiss (close) this announcement', verbose_name='Dismissable')),
                ('button_dismiss_text', models.CharField(help_text='Text displayed with the dismiss button', max_length=100, verbose_name='Dismiss text', blank=True)),
                ('announcement_type', models.IntegerField(default=0, verbose_name='Announcement type', choices=[(0, 'Modal')])),
                ('template', models.CharField(default='', max_length=200)),
                ('expire_days', models.PositiveSmallIntegerField(help_text='Show the announcement again after being dismissed after this amount of days', null=True, verbose_name='Announcement frequency', blank=True)),
                ('appearance_delay', models.IntegerField(default=0, help_text='Delay time for the announcement to appear (miliseconds)', verbose_name='Appearance delay')),
                ('form', models.ForeignKey(blank=True, to='forms.Form', null=True)),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
        ),
    ]
