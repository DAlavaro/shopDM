from django import template

from fallout_shelter.models import Category

register = template.Library()


@register.simple_tag(name="category")
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag("fallout_shelter/list_categories.html")
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

@register.filter()
def mymedia(value):
    if value:
        return f'/media/{value}'
    else:
        return '#'
