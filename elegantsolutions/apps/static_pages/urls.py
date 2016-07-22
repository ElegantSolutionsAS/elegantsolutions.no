from __future__ import unicode_literals

from django.conf.urls import url, patterns
from django.views.decorators.cache import cache_page

from .views import TeaserPage


app_name = "static_pages"

urlpatterns = patterns(
    'static_pages.views',

    url(r'^/?$', cache_page(1800)(TeaserPage.as_view()), name="teaser"),
)
