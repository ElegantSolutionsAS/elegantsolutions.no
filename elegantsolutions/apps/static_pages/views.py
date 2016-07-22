from __future__ import unicode_literals

from django.views.generic import TemplateView


class TeaserPage(TemplateView):
    """
    Teaser view for elegant solutions.

    Static page that needs to be in place until we get proper website :o)
    """

    template_name = 'static_pages/teaser.html'
    document_title = 'Elegant Solutions AS'
