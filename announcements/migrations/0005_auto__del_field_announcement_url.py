# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Announcement.url'
        db.delete_column(u'announcements_announcement', 'url')


    def backwards(self, orm):
        # Adding field 'Announcement.url'
        db.add_column(u'announcements_announcement', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    models = {
        u'announcements.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'can_dismiss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {'default': "''"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['announcements']