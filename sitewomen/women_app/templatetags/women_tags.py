from django import template
from women_app.models import *


register = template.Library()


@register.inclusion_tag('women_app/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('women_app/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}