from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [url(r"^current/$", views.announcements_json)]
