from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter

def color_lookup(tuple, key):
    return dict(tuple).get(key, "Unknown Color")
