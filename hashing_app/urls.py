from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render_to_response

from urls_hash.views import UrlHashView, HashedUrlView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', UrlHashView.as_view(), name='new_hash'),
    url(r'^(?P<hash_value>.*)/$', HashedUrlView.as_view(), name='hashed_url'),
]


# pylint: disable=unused-argument
def handler404(request, *args, **argv):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response
