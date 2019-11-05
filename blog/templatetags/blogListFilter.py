from django import template

register = template.Library()


@register.filter
def key(value, arg):
    return value[arg]
