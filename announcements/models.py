from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.template import RequestContext, loader

from mezzanine.conf import settings
from mezzanine.core.models import CurrentSiteManager
from mezzanine.core.models import SiteRelated
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.request import current_request
from mezzanine.forms.forms import FormForForm


class AnnouncementManager(CurrentSiteManager):
    """
    Custom manager for the Announcement model.
    """

    def current(self):
        """
        Return the currently active announcements.
        """
        now = timezone.now()
        return self.filter(date_start__lte=now).filter(
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
        return qs


@python_2_unicode_compatible
class Announcement(SiteRelated):
    """
    An announcement to all site visitors.
    Announcements can be scheduled and/or dismissed by each user when seen.
    """

    title = models.CharField("Title", max_length=255)
    content = RichTextField("Content")
    extra_content = RichTextField("Extra Content (optional)", blank=True)
    image = FileField(
        "Image", upload_to="announcements/images", format="Image", blank=True
    )

    date_created = models.DateTimeField(
        "Date created", db_index=True, auto_now_add=True
    )
    date_start = models.DateTimeField("Start date", db_index=True, default=now)
    date_end = models.DateTimeField("End date", db_index=True, null=True, blank=True)

    can_dismiss = models.BooleanField(
        "Dismissable",
        default=True,
        help_text="The user can dismiss (close) this announcement",
    )
    button_dismiss_text = models.CharField(
        "Dismiss text",
        max_length=100,
        blank=True,
        help_text="Text displayed with the dismiss button",
    )
    template = models.CharField(max_length=200)
    form = models.ForeignKey("forms.Form", blank=True, null=True)
    video_link = models.URLField("Video URL", blank=True)
    expire_days = models.PositiveIntegerField(
        "Announcement frequency",
        default=365,
        help_text="Show the announcement again after being dismissed after "
        "this amount of days",
    )
    appearance_delay = models.PositiveIntegerField(
        "Appearance delay",
        default=0,
        help_text="Delay time for the announcement to appear (milliseconds)",
    )

    objects = AnnouncementManager()

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
        ordering = ["-date_start"]

    def __str__(self):
        return self.title

    def get_template_display(self):
        templates = dict(settings.ANNOUNCEMENTS_TEMPLATES)
        return templates.get(self.template, "")

    get_template_display.short_description = "Template"

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
        t = loader.get_template(self.template)
        return t.render({"announcement": self})

    def to_json(self):
        """
        JSON representation of this announcement.
        """
        return {
            "id": self.pk,
            "title": self.title,
            "can_dismiss": self.can_dismiss,
            "html": self.to_html(),
        }
