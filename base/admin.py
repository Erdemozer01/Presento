from django.contrib import admin

from .models import Inbox
from .models import (
    Home, AboutTab, Hero, Clients, Services, FrequentlyAskedQuestions,
    Team, AboutCategory, Contact, Subscriber, MetaTags, SocialNetwork
)

class SocialNetworkAdmin(admin.StackedInline):
    model = SocialNetwork
    extra = 0
    classes = ['collapse']

class MetaTagsInline(admin.TabularInline):
    model = MetaTags
    extra = 0
    classes = ['collapse']


class FrequentlyAskedQuestionsAdmin(admin.StackedInline):
    model = FrequentlyAskedQuestions
    extra = 0
    classes = ['collapse']


class ServicesAdmin(admin.StackedInline):
    model = Services
    extra = 0
    classes = ['collapse']


class ClientsAdmin(admin.StackedInline):
    model = Clients
    extra = 0
    classes = ['collapse']


class HeroAdmin(admin.StackedInline):
    model = Hero
    extra = 0
    classes = ['collapse']

    def has_add_permission(self, request, obj=None):
        if Hero.objects.count() == 0:
            return True
        return False


@admin.register(AboutCategory)
class AboutAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class AboutTabAdmin(admin.StackedInline):
    model = AboutTab
    extra = 0
    classes = ['collapse']


class TeamAdmin(admin.StackedInline):
    model = Team
    extra = 0
    classes = ['collapse']


class ContactAdmin(admin.StackedInline):
    model = Contact
    extra = 0
    classes = ['collapse']

    def has_add_permission(self, request, obj):
        if Contact.objects.exists():
            return False
        else:
            return True


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    inlines = [
        MetaTagsInline, HeroAdmin, ClientsAdmin, AboutTabAdmin, ServicesAdmin,
        TeamAdmin, FrequentlyAskedQuestionsAdmin, ContactAdmin, SocialNetworkAdmin
    ]

    list_display = ('name', 'email', 'created', 'updated')

    fieldsets = [
        ('Temel Ayarlar', {'fields': ['name', 'email', 'email_password'], "classes": ['wide']}),
    ]

    def has_add_permission(self, request):
        if Home.objects.exists():
            return False
        else:
            return True


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'is_read', 'created',)
    search_fields = ['subject', 'name', 'email']
    search_help_text = 'Konu, ad, email'
    list_filter = ('created', 'is_read')

    def has_add_permission(self, request):
        return False

    def changeform_view(self, request, object_id=..., form_url=..., extra_context=...):
        obj = self.get_object(request, object_id)
        obj.is_read = True
        obj.save()
        return super().changeform_view(request, object_id, form_url, extra_context)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)

    def has_add_permission(self, request):
        return False



