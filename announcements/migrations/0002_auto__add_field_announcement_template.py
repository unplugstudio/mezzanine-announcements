# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Announcement.template'
        db.add_column(u'announcements_announcement', 'template',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Announcement.template'
        db.delete_column(u'announcements_announcement', 'template')


    models = {
        u'announcements.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'announcement_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'can_dismiss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['announcements']