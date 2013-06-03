from django.shortcuts import get_object_or_404
from flis.models import Country


class CountryMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.path.startswith('/management'):
            request.country = get_object_or_404(Country,
                pk=view_kwargs.pop('country'))
        else:
            request.country = None
