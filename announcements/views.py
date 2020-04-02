from announcements.models import Announcement

from django.http import JsonResponse


def announcements_json(request):
    """
    Return the current announcements as JSON
    """
    announcements = Announcement.objects.for_request(request)

    return JsonResponse([a.to_json() for a in announcements], safe=False)
