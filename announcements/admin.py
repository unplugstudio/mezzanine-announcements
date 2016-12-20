from django.contrib import admin

from mezzanine.conf import settings

from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    exclude = ['template']
    list_display = ['title', 'announcement_type', 'date_start', 'date_end', 'is_active',
                    'can_dismiss']
    list_filter = ['announcement_type', 'can_dismiss']
    date_hierarchy = 'date_start'

    def get_form(self, request, obj=None, **kwargs):
        if not settings.ANNOUNCEMENTS_VIDEO_ENABLED:
            if self.exclude is not None:
                self.exclude.append("video_link")
            else:
                self.exculde = ["video_link"]
        print self.exclude
        form = super(AnnouncementAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(Announcement, AnnouncementAdmin)
