from django import template

register = template.Library()


@register.filter()
def type_filter(value: str):
    try:
        float(value)
    except Exception(''):
        return 0
    return float(value)
