from django.contrib import admin

from .models import Announcement


class AnnouncementOptions(admin.ModelAdmin):
    list_display = ['title', 'date_start', 'date_end', 'is_current', 'announcement_type']

admin.site.register(Announcement, AnnouncementOptions)
