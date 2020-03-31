from __future__ import unicode_literals, absolute_import

from copy import deepcopy

from django.contrib import admin

from mezzanine.conf import settings

from .models import Announcement

base_fieldsets = [
    ("Content", {"fields": ["image", "title", "content", "announcement_type"]}),
    ("Schedule", {"fields": [("date_start", "date_end")]}),
    (
        "Settings",
        {
            "classes": ["collapse-closed"],
            "fields": ["can_dismiss", "button_dismiss_text", "expire_days", "appearance_delay"],
        },
    ),
]


class AnnouncementAdmin(admin.ModelAdmin):
    date_hierarchy = "date_start"
    list_filter = ["announcement_type", "can_dismiss"]
    list_display = [
        "title",
        "announcement_type",
        "date_start",
        "date_end",
        "is_active",
        "can_dismiss",
    ]

    def get_fieldsets(self, request, obj=None):
        """
        Inject customizable fields from settings
        """
        fieldsets = deepcopy(base_fieldsets)
        extras = settings.ANNOUNCEMENTS_EXTRA_FIELDS
        if extras is not None:
            fieldsets[0][1]["fields"] += extras
        return fieldsets


admin.site.register(Announcement, AnnouncementAdmin)
