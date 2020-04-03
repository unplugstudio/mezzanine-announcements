# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_template_field_refactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='appearance_delay',
            field=models.PositiveIntegerField(default=0, help_text='Delay time for the announcement to appear (milliseconds)', verbose_name='Appearance delay'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='expire_days',
            field=models.PositiveIntegerField(default=365, help_text='Show the announcement again after being dismissed after this amount of days', verbose_name='Announcement frequency'),
        ),
    ]
