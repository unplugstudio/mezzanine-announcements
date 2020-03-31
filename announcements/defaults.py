
from mezzanine.conf import register_setting

register_setting(
    name="ANNOUNCEMENTS_MAX_NUMBER",
    description="The total number of announcements to be displayed at the same time, "
                "according to the date and time that the announcements "
                "will be published.",
    editable=True,
    default=1
)

register_setting(
    name="ANNOUNCEMENTS_EXTRA_FIELDS",
    editable=False,
    default=None
)

register_setting(
    name="ANNOUNCEMENTS_RICHTEXT_CONTENT",
    editable=False,
    default=False
)
