from django import template
from django.contrib.auth.models import Group


register = template.Library()
@register.filter(name='w_grupie') 
def w_grupie(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False 

register.inclusion_tag('cpracownik/pracList.html')(w_grupie)
