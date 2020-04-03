from __future__ import unicode_literals, absolute_import

from copy import deepcopy

from django import forms
from django.contrib import admin
from django.db import models

from mezzanine.conf import settings
from mezzanine.core.forms import TinyMceWidget

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    """
    Dynamically get the template options from settings
    """

    template = forms.ChoiceField(
        choices=settings.ANNOUNCEMENTS_TEMPLATES, label="Template"
    )

    class Meta:
        model = Announcement
        fields = "__all__"


base_fieldsets = [
    ("Content", {"fields": ["image", "title", "template", "content"]}),
    ("Schedule", {"fields": [("date_start", "date_end")]}),
    (
        "Settings",
        {
            "classes": ["collapse-closed"],
            "fields": [
                "can_dismiss",
                "button_dismiss_text",
                "expire_days",
                "appearance_delay",
            ],
        },
    ),
]


class AnnouncementAdmin(admin.ModelAdmin):
    form = AnnouncementForm
    date_hierarchy = "date_start"
    list_filter = ["can_dismiss"]
    list_display = [
        "title",
        "get_template_display",
        "date_start",
        "date_end",
        "is_active",
        "can_dismiss",
    ]

    def __init__(self, model, admin_site):
        """
        Apply customizations from settings
        """
        super(AnnouncementAdmin, self).__init__(model, admin_site)

        if settings.ANNOUNCEMENTS_RICHTEXT_CONTENT:
            self.formfield_overrides[models.TextField] = {"widget": TinyMceWidget}

        self.fieldsets = deepcopy(base_fieldsets)
        extras = settings.ANNOUNCEMENTS_EXTRA_FIELDS
        if extras is not None:
            self.fieldsets[0][1]["fields"] += extras


admin.site.register(Announcement, AnnouncementAdmin)
