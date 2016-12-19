from django.contrib import admin

from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    exclude = ['template']
    list_display = ['title', 'announcement_type', 'date_start', 'date_end', 'is_active',
                    'can_dismiss']
    list_filter = ['announcement_type', 'can_dismiss']
    date_hierarchy = 'date_start'


admin.site.register(Announcement, AnnouncementAdmin)
