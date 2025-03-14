from django import template

register = template.Library()


@register.filter(name='breadcrumbs')
def breadcrumbs(crumbs):
    return crumbs.rsplit('/', 2)[1].title().replace('-', ' ').replace('#', ' ')
