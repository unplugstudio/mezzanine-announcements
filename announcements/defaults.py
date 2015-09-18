from django.conf import settings

ANNOUNCEMENTS_JS_NAMESPACE = getattr(settings, 'ANNOUNCEMENTS_JS_NAMESPACE', 'Announcements')

ANNOUNCEMENTS_COOKIE_NAME = getattr(settings, 'ANNOUNCEMENTS_COOKIE_NAME', 'announcements_dismiss')

ANNOUNCEMENTS_MAX = getattr(settings, "ANNOUNCEMENTS_MAX", 1)
