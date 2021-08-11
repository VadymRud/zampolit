from django import template
from staff.models import Name
register = template.Library()

@register.simple_tag
def get(value):

    try:
        name = Name.objects.filter(pos_id=value)
    except Name.DoesNotExist:
        name = 'vacant'
   
    return name

# register.filter('get', get)