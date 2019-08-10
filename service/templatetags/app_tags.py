from __future__ import unicode_literals
from django import template

register = template.Library()


@register.filter
def partition(data, n):
    try:
        n = int(n)
    except (ValueError, TypeError):
        return [data]

    return [data[i:i + n] for i in range(0, len(data), n)]
