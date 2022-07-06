from django import template

from news.models import Category

register = template.Library()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
