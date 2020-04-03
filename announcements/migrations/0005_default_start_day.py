# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0004_expire_days_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start date', db_index=True),
        ),
    ]
