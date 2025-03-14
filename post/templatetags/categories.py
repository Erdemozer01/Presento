from django import template
from post.models.article import ArticleCategory

register = template.Library()

@register.simple_tag
def categories_list():
    return ArticleCategory.objects.all()