from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from mezzanine.conf import settings
from mezzanine.core.fields import RichTextField


class AnnouncementManager(models.Manager):
    """
    Custom manager for the Announcement model.
    """

    def current(self):
        """
        Return the currently active announcements.
        """
        now = timezone.now()
        return self.get_query_set().filter(date_start__lte=now).filter(
            models.Q(date_end__gte=now) | models.Q(date_end__isnull=True)
        )

    def for_request(self, request):
        """
        Return the announcements for the current request/session.
        """
        from announcements import defaults
        cookie_name = defaults.ANNOUNCEMENTS_COOKIE_NAME
        cookie = request.COOKIES.get(cookie_name, None)

        dismissed_pk = 0
        if cookie:
            try:
                dismissed_pk = int(cookie)
            except ValueError:
                pass

        qs = self.current().filter(pk__gt=dismissed_pk)
        qs = qs.order_by('-date_start')[:settings.ANNOUNCEMENTS_MAX_NUMBER]
        return qs


@python_2_unicode_compatible
class Announcement(models.Model):
    """
    An announcement to all site visitors.
    Announcements can be scheduled and/or dismissed by each user when seen.
    """
    title = models.CharField("Title", max_length=255)
    content = RichTextField("Content")
    date_created = models.DateTimeField(
        "Date created", db_index=True, auto_now_add=True)
    date_start = models.DateTimeField(
        "Start date", db_index=True)
    date_end = models.DateTimeField(
        "End date", db_index=True, null=True, blank=True)
    can_dismiss = models.BooleanField(
        "Dismissable", default=True,
        help_text="The user can dismiss (close) this announcement")
    announcement_type = models.IntegerField(
        "Announcement type", default=1, choices=settings.ANNOUNCEMENTS_TYPES,
        help_text="This controls how the announcement will be displayed")

    objects = AnnouncementManager()

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title

    def is_active(self):
        """
        Helper method to determine if the announcement is currently active.
        """
        now = timezone.now()
        if self.date_start < now:
            if self.date_end is None or self.date_end > now:
                return True
        return False
    is_active.boolean = True

    def to_html(self):
        """
        HTML representation of this announcement.
        """
        from django.template import loader, Context
        t = loader.get_template("announcements/announcement.html")
        c = Context({
            'announcement': self,
        })
        return t.render(c)

    def to_json(self):
        """
        JSON representation of this announcement.
        """
        return {
            'id': self.pk,
            'title': self.title,
            'can_dismiss': self.can_dismiss,
            'html': self.to_html(),
        }
