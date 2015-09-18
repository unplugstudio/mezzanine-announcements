# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Announcement.content'
        db.add_column(u'announcements_announcement', 'content',
                      self.gf('mezzanine.core.fields.RichTextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Announcement.content'
        db.delete_column(u'announcements_announcement', 'content')


    models = {
        u'announcements.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'content': ('mezzanine.core.fields.RichTextField', [], {'default': "''"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['announcements']