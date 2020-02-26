from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def site_name():
    """
    Include site name.
    """
    return settings.SITE_NAME