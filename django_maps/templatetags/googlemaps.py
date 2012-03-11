"""
Map functionality implemented using Google Maps.

You should probably put ``GOOGLEMAPS_KEY = "your-api-key"`` in your settings
if you use this.
"""

from django import template
from django.conf import settings
from django.utils import simplejson as json


API_KEY = getattr(settings, 'GOOGLEMAPS_KEY', None)

# a context variable to store the javascript global variable name for
# the last-created map object
MAP_NAME_CONTEXT_VARIABLE = '__last_added_map__'


register = template.Library()


@register.inclusion_tag('django_maps/googlemaps.html', takes_context=True)
def map(context, selector, **options):
    """
    Initialize a map in a DOM element given by a jQuery selector.

    Example::

      {% map '#my-map' %}
    """
    defaults = {
        'var_name': 'Map'
    }
    context.update(defaults)
    context.update(options)
    context.update({
        'selector': selector,
        'API_KEY': API_KEY,
        'api_loaded': MAP_NAME_CONTEXT_VARIABLE in context,
        MAP_NAME_CONTEXT_VARIABLE: context['var_name'],
    })
    return context


@register.inclusion_tag('django_maps/add_route.html', takes_context=True)
def add_route(context, points, **options):
    """
    Draw a route on a map.
    """
    try:
        map = options.pop('map', context[MAP_NAME_CONTEXT_VARIABLE])
    except KeyError:
        raise template.TemplateSyntaxError(
            '`add_route` tag can only be called after initializing a map '
            'using the `map` tag')

    context.update({
        'map': map,
        'points': json.dumps(points, ensure_ascii=False),
        'options': json.dumps(options, ensure_ascii=False),
    })
    return context
