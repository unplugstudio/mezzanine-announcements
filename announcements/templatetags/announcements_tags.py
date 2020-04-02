import urlparse

from announcements import defaults
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def dismiss_js_link(a):
    return mark_safe(
        u"%s.dismiss('%s', '%s')"
        % (
            defaults.ANNOUNCEMENTS_JS_NAMESPACE,
            defaults.ANNOUNCEMENTS_COOKIE_NAME,
            a.pk,
        )
    )


@register.filter
def generate_video_iframe(url):
    """
    Filter used to construct an iframe element from an URL of a video, either
    from YouTube or Vimeo.
    """
    hostname = ""
    video_type = ""
    video_id = None
    # This setting is to make possible to speak with the API of YouTube videos
    # using JavaScript.
    enable_js_api = ""

    url_data = urlparse.urlparse(url)

    if url_data.hostname in ("www.vimeo.com", "vimeo.com"):
        hostname = "player.vimeo.com"
        video_type = "video"
        video_id = url_data.path[1:]

    if url_data.hostname in ("www.youtube.com", "youtube.com", "youtu.be"):
        hostname = "www.youtube.com"
        video_type = "embed"
        enable_js_api = "enablejsapi=1"  # Enable this only for YouTube videos.
        if url_data.hostname == "youtu.be":
            video_id = url_data.path[1:]
        if video_id is None:
            query = urlparse.parse_qs(url_data.query)
            video_id = query["v"][0]

    return (
        "<iframe src='https://{hostname}/{type}/{id}?autoplay=1&{enable_js_api}' "
        "frameborder='0' allowfullscreen></iframe>".format(
            hostname=hostname, type=video_type, id=video_id, enable_js_api=enable_js_api
        )
    )
