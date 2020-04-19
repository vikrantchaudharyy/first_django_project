from django import template

register = template.Library()

@register.filter(name='cutter')
def cutter(value,args):
    """
    This cuts out the value 'args' from the string!
    """
    return value.replace(args,"")

 # register.filter('cutter',cutter)
