"""Views for the general application."""

from django.http import HttpResponse
from django.core.management import call_command


def cron_rebuild_index(request):
    """Rebuild search index when triggered by cron job.

    Returns:
        200 HTTP response when valid cron job call is made.
        403 HTTP resoponse when invalid source.
    """
    if request.META.get('HTTP_X_APPENGINE_CRON'):
        call_command('rebuild_index', noinput='')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)
