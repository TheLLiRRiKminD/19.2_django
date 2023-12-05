from django import template

register = template.Library()

# Создание тега
@register.simple_tag
def mediapath():
    return "/media/"
