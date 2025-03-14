from django import template
from base.models.home import Home, FrequentlyAskedQuestions, Services, Hero, AboutTab, AboutCategory, Team, Clients, \
    Contact, MetaTags

register = template.Library()


@register.simple_tag
def meta_tags():
    try:
        return MetaTags.objects.all()
    except MetaTags.DoesNotExist:
        return None


@register.simple_tag
def base_settings():
    try:
        return Home.objects.latest('created')
    except Home.DoesNotExist:
        return None


@register.simple_tag
def clients():
    try:
        return Clients.objects.all()
    except Clients.DoesNotExist:
        return []


@register.simple_tag
def about_category():
    return AboutCategory.objects.all()


@register.simple_tag
def about():
    try:
        return AboutTab.objects.all()
    except AboutTab.DoesNotExist:
        return None


@register.simple_tag
def hero_list():
    try:
        return Hero.objects.all()
    except Hero.DoesNotExist:
        return None


@register.simple_tag
def frequently_asked_question():
    try:
        return FrequentlyAskedQuestions.objects.all()
    except FrequentlyAskedQuestions.DoesNotExist:
        return None


@register.simple_tag
def services_list():
    try:
        return Services.objects.all()
    except Services.DoesNotExist:
        return None


@register.simple_tag
def teams_list():
    try:
        return Team.objects.all()
    except Team.DoesNotExist:
        return None


@register.simple_tag
def contact():
    try:
        return Contact.objects.latest('created')
    except Contact.DoesNotExist:
        return None


@register.filter(name='replace')
def replace(value, old):
    return value.replace(old, '').replace(' ', '').replace('bi', '')

