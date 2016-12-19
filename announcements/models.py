from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.template import RequestContext

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.request import current_request
from mezzanine.forms.forms import FormForForm


# Announcements types tuple
ANNOUNCEMENTS_TYPES = []
for index, value in enumerate(settings.ANNOUNCEMENT_TEMPLATES):
    ANNOUNCEMENTS_TYPES.append((index, value[1]))


class AnnouncementManager(models.Manager):
    """
    Custom manager for the Announcement model.
    """

    def current(self):
        """
        Return the currently active announcements.
        """
        now = timezone.now()
        return self.get_queryset().filter(date_start__lte=now).filter(
            models.Q(date_end__gte=now) | models.Q(date_end__isnull=True)
        )

    def for_request(self, request):
        """
        Return the announcements for the current request/session.
        """
        cookie_name = "announcements_dismiss"
        cookie = request.COOKIES.get(cookie_name, None)
        try:
            cookie = cookie.split("_")
            cookie = [int(x) for x in cookie]
        except AttributeError:
            pass
        dismissed_pk = [0]
        if cookie:
            try:
                dismissed_pk = cookie
            except ValueError:
                pass

        qs = self.current().exclude(pk__in=dismissed_pk)
        qs = qs.order_by('-date_start')[:settings.ANNOUNCEMENTS_MAX_NUMBER]
        return qs


@python_2_unicode_compatible
class Announcement(models.Model):
    """
    An announcement to all site visitors.
    Announcements can be scheduled and/or dismissed by each user when seen.
    """
    title = models.CharField("Title", max_length=255)
    content = models.TextField("Content")
    date_created = models.DateTimeField(
        "Date created", db_index=True, auto_now_add=True)
    date_start = models.DateTimeField(
        "Start date", db_index=True)
    date_end = models.DateTimeField(
        "End date", db_index=True, null=True, blank=True)
    image = FileField(
        "Image", upload_to="announcements/images", format="Image", blank=True)
    can_dismiss = models.BooleanField(
        "Dismissable", default=True,
        help_text="The user can dismiss (close) this announcement")
    button_dismiss_text = models.CharField(
        "Dismiss text", max_length=100, blank=True,
        help_text="Text displayed with the dismiss button")
    announcement_type = models.IntegerField(
        "Announcement type", default=0, choices=ANNOUNCEMENTS_TYPES)
    template = models.CharField(max_length=200, default="")
    form = models.ForeignKey("forms.Form", blank=True, null=True)
    expire_days = models.PositiveSmallIntegerField(
        "Announcement frequency", null=True, blank=True,
        help_text="Show the announcement again after being dismissed after "
        "this amount of days")
    appearance_delay = models.IntegerField(
        "Appearance delay", default=0,
        help_text="Delay time for the announcement to appear (miliseconds)")

    objects = AnnouncementManager()

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.template = settings.ANNOUNCEMENT_TEMPLATES[self.announcement_type][0]
        super(Announcement, self).save(*args, **kwargs)

    def get_email_form(self):
        if self.form:
            return FormForForm(self.form, RequestContext(current_request()), None, None)
        return None

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
