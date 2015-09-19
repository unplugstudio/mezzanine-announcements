from django.conf import settings

from mezzanine.conf import register_setting

ANNOUNCEMENTS_JS_NAMESPACE = getattr(settings, 'ANNOUNCEMENTS_JS_NAMESPACE', 'Announcements')

ANNOUNCEMENTS_COOKIE_NAME = getattr(settings, 'ANNOUNCEMENTS_COOKIE_NAME', 'announcements_dismiss')

ANNOUNCEMENTS_MAX = getattr(settings, "ANNOUNCEMENTS_MAX", 1)

register_setting(
    name="ANNOUNCEMENTS_TYPES",
    description="The types of announcements that the user can choose."
                "Depends to the developer how to display the announcement.",
    editable=False,
    default=[(1, "Top bar"), (2, "Roadblock (splash screen)"),],
)
