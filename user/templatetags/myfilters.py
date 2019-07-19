from django import template

register = template.Library()

@register.filter('multiply')
def multiply(a, b): # x|add:5
    print(a, b)
    return int(a) * int(b)
