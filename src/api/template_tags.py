from django import template
from django.urls import NoReverseMatch, reverse
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def userlinks_list(request, user):
    """
    Include navbar menu list items.
    """
    items = []

    extra_items = userlinks_extras(request, user)
    if extra_items and len(extra_items) > 0:
        items += extra_items

    if not user.is_authenticated:
        title = "Not logged in"
        items.append(userlinks_login(request))
    else:
        title = user.username
        items.append(userlinks_logout(request))

    if len(items) == 0:
        return ""

    content = """
        <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                {title}
                <b class="caret"></b>
            </a>
            <ul class="dropdown-menu">
        """
    content = format_html(content, title=escape(title))
    for item in items:
        content += item + "\n"
    content += """
            </ul>
        </li>
    """

    return mark_safe(content)  # noqa: S703, S308 (potential XSS)


def userlinks_login(request):
    try:
        item = '<li><a href="{href}?next={next}">Log in</a></li>'
        return format_html(item, href=reverse("rest_framework:login"), next=escape(request.path))
    except NoReverseMatch:
        pass


def userlinks_logout(request):
    try:
        item = '<li><a href="{href}?next={next}">Log out</a></li>'
        return format_html(item, href=reverse("rest_framework:logout"), next=escape(request.path))
    except NoReverseMatch:
        pass


def userlinks_extras(request, user):
    items = []
    general_item = '<li><a href="{href}">{name}</a></li>'

    # Link to API
    items.append(format_html(general_item, name="API", href=reverse("api")))

    # Link to site scheme
    items.append(format_html(general_item, name="Schema", href=reverse("schema")))

    if user.is_staff:
        items.append(format_html(general_item, name="Admin", href=reverse("admin:index")))

    return items
