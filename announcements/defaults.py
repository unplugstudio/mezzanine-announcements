from django.conf import settings

from mezzanine.conf import register_setting

ANNOUNCEMENTS_JS_NAMESPACE = getattr(settings, 'ANNOUNCEMENTS_JS_NAMESPACE', 'Announcements')

ANNOUNCEMENTS_COOKIE_NAME = getattr(settings, 'ANNOUNCEMENTS_COOKIE_NAME', 'announcements_dismiss')

register_setting(
    name="ANNOUNCEMENTS_MAX_NUMBER",
    description="The total number of announcements to be displayed at the same time, "
                "according to the date and time that the announcements "
                "will be published.",
    editable=True,
    default=1
)

register_setting(
    name="ANNOUNCEMENTS_TYPES",
    description="The types of announcements that the user can choose."
                "Depends to the developer how to display the announcement.",
    editable=False,
    default=[(1, "Top bar"), (2, "Roadblock (splash screen)"),],
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description="Make ANNOUNCEMENTS_TYPES to be accesible in template.",
    editable=False,
    default=("ANNOUNCEMENTS_TYPES",),
    append=True,
)
