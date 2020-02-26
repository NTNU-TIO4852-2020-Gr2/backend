from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def google_maps_api_key():
    """
    Include site name.
    """
    return settings.GOOGLE_MAPS_API_KEY


@register.simple_tag
def google_maps_latitude():
    """
    Include site name.
    """
    return settings.GOOGLE_MAPS_LATITUDE


@register.simple_tag
def google_maps_longitude():
    """
    Include site name.
    """
    return settings.GOOGLE_MAPS_LONGITUDE


@register.simple_tag
def google_maps_zoom():
    """
    Include site name.
    """
    return settings.GOOGLE_MAPS_ZOOM


@register.simple_tag
def google_maps_type():
    """
    Include site name.
    """
    return settings.GOOGLE_MAPS_TYPE
