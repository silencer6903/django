from django import template
import library.views as views

register = template.Library()


@register.simple_tag
def catalog():
    cats = views.cats
    return cats

@register.inclusion_tag('library/lef_catalog.html')
def left_catalog_list(cat_id=0):
    return {'cats': views.cats, 'cat_id': cat_id}