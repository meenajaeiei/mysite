from django import template
from graphweb.models import *


register = template.Library()

@register.inclusion_tag('latest_posts.html')
def show_history():
    print("kasdasdsadczxcx")
    return {"history_list" : History.published.get_queryset() }


@register.inclusion_tag('latest_posts.html')
def show_head_history(number):
    count = 0
    try:
        return {"history_list" :  History.published.all()[History.published.count()-number:History.published.count()] }
        
    except:
        return {"history_list" : History.published.get_queryset() }
    
        
        