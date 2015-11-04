# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Announcement.image'
        db.add_column(u'announcements_announcement', 'image',
                      self.gf('mezzanine.core.fields.FileField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Announcement.button_dismiss_text'
        db.add_column(u'announcements_announcement', 'button_dismiss_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Announcement.template'
        db.add_column(u'announcements_announcement', 'template',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=200),
                      keep_default=False)

        # Adding field 'Announcement.expire_days'
        db.add_column(u'announcements_announcement', 'expire_days',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Announcement.content'
        db.alter_column(u'announcements_announcement', 'content', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting field 'Announcement.image'
        db.delete_column(u'announcements_announcement', 'image')

        # Deleting field 'Announcement.button_dismiss_text'
        db.delete_column(u'announcements_announcement', 'button_dismiss_text')

        # Deleting field 'Announcement.template'
        db.delete_column(u'announcements_announcement', 'template')

        # Deleting field 'Announcement.expire_days'
        db.delete_column(u'announcements_announcement', 'expire_days')


        # Changing field 'Announcement.content'
        db.alter_column(u'announcements_announcement', 'content', self.gf('mezzanine.core.fields.RichTextField')())

    models = {
        u'announcements.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'announcement_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'button_dismiss_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'can_dismiss': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'expire_days': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['announcements']