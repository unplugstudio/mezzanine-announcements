from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured


class AnnouncementsConfig(AppConfig):
    name = "announcements"
    verbose_name = "Announcements"

    def __init__(self, app_name, app_module):
        super(AnnouncementsConfig, self).__init__(app_name, app_module)

        from mezzanine.conf import settings

        if hasattr(settings, "ANNOUNCEMENTS_VIDEO_ENABLED"):
            raise ImproperlyConfigured(
                "`settings.ANNOUNCEMENTS_VIDEO_ENABLED` has been deprecated. "
                "Please use `settings.ANNOUNCEMENTS_EXTRA_FIELDS = ['video_link']`"
            )

        if hasattr(settings, "ANNOUNCEMENTS_RICHTEXT_CONTENT"):
            raise ImproperlyConfigured(
                "`settings.ANNOUNCEMENTS_RICHTEXT_CONTENT` has been deprecated. "
                "All content fields are now RichText fields."
            )

        if not hasattr(settings, "ANNOUNCEMENTS_TEMPLATES"):
            raise ImproperlyConfigured(
                "You must define settings.ANNOUNCEMENTS_TEMPLATES to use "
                "mezzanine-announcements"
            )
