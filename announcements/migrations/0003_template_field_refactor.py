# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_add_extra_content_video_link_and_announcement_type_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='announcement_type',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='template',
            field=models.CharField(max_length=200),
        ),
    ]
