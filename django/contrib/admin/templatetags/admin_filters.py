from django import template
from django.contrib.admin.options import EMPTY_VALUE_STRING
from django.contrib.admin.utils import display_for_value
from django.template.defaultfilters import stringfilter, unordered_list

register = template.Library()


@register.filter
@stringfilter
def to_object_display_value(value):
    return display_for_value(str(value), EMPTY_VALUE_STRING)


@register.filter(is_safe=True, needs_autoescape=True)
def truncated_unordered_list(value, max_items, autoescape=True):
    """
    Render an unordered list, showing at most ``max_items`` items and a
    "...and N more." suffix for the rest.

    Usage::

        {{ deleted_objects|truncated_unordered_list:100 }}
    """
    try:
        max_items = int(max_items)
    except (TypeError, ValueError):
        return unordered_list(value, autoescape=autoescape)
    return unordered_list(value, autoescape=autoescape, max_items=max_items)
