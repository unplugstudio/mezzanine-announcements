
from django.db import models
from django.utils import timezone

from mezzanine.core.fields import RichTextField

class AnnouncementManager(models.Manager):
    def current(self):
        now = timezone.now()
        return self.get_query_set().filter(date_start__lte=now).filter(
            models.Q(date_end__gte=now) | models.Q(date_end__isnull=True)
        )

    def for_request(self, request):
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
        qs = qs.order_by('-date_start')[:defaults.ANNOUNCEMENTS_MAX]
        return qs

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(default="")
    date_created = models.DateTimeField(db_index=True, auto_now_add=True)
    date_start = models.DateTimeField(db_index=True)
    date_end = models.DateTimeField(db_index=True, null=True, blank=True)
    can_dismiss = models.BooleanField(
        "Can be dismissed", default=True, help_text="Announcement can be dismissed")

    objects = AnnouncementManager()

    def is_current(self):
        now = timezone.now()
        if self.date_start < now:
            if self.date_end is None or self.date_end > now:
                return True
        return False

    # for great justice. (and admin prettiness)
    is_current.boolean = True

    def __unicode__(self):
        return unicode(self.title)

    def to_html(self):
        from django.template import loader, Context
        t = loader.get_template("announcements/announcement.html")
        c = Context({
            'announcement': self,
        })
        return t.render(c)

    def to_json(self):

        return {
            'id': self.pk,
            'title': self.title,
            'can_dismiss': self.can_dismiss,
            'html': self.to_html(),
        }
