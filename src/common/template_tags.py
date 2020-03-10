from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def site_name():
    """
    Include site name.
    """
    return settings.SITE_NAME


@register.simple_tag
def logo_link():
    """
    Include logo link.
    """
    return settings.LOGO_LINK
