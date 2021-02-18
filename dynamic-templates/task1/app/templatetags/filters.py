from django import template

register = template.Library()


@register.filter()
def color_filter(value):
    if value == '-':
        return "#ffffff"
    elif float(value) > 1000:
        return "#ffffff"
    elif float(value) < 0:
        return "darkgreen"
    elif 1 < float(value) < 2:
        return "#ffa48f"
    elif 2 < float(value) < 5:
        return "#fe6f5e"
    elif float(value) > 5:
        return "red"
    else:
        return "#ffffff"


@register.filter()
def get_keys_filer(value: dict):
    return list(value.keys())


@register.filter()
def get_value(key, dictionary):
    return dictionary[key]


