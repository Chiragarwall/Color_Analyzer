from django import template

register = template.Library()

@register.filter(name='inttohex')
def inttohex(value):
    print("Filter executed")
    return hex(value)[2:]
