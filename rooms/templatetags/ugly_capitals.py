from django import template

register = template.Library()


@register.filter
def ugly_capitals(value):
    return value.capitalize()
