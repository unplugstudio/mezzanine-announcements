
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
    name="ANNOUNCEMENTS_VIDEO_ENABLED",
    description="If `True` it will be possible to embed a video in the announcement.",
    editable=False,
    default=False
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("ANNOUNCEMENTS_VIDEO_ENABLED",),
)
