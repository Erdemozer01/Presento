import os
from pathlib import Path
from smtplib import SMTPAuthenticationError

from django.contrib import admin, messages
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template

from .models.portfolio import Portfolio, PortFolioAddContentModel, PortfolioCategory
from .models.article import ArticleModel, ArticleTags, ArticleComment, ArticleCategory
from .models import NewsLetterModel
from django.conf import settings
from base.models import Home, Subscriber

BASE_DIR = Path(__file__).resolve().parent.parent


@admin.register(NewsLetterModel)
class NewsLetterModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
    list_filter = ('created',)
    actions = ['send_email']

    @admin.action(description='Seçtiğiniz konuyu abonelere e-posta ile gönder')
    def send_email(self, request, queryset):

        try:
            site = Home.objects.latest('created')
            settings.EMAIL_HOST_USER = site.email
            settings.EMAIL_HOST_PASSWORD = site.email_password
        except Home.DoesNotExist:
            site = None
            messages.error(request, "Site ayarları yapılandırılmamış")

        # E-posta gönderim işlemi
        try:
            connection = mail.get_connection()
            connection.open()  # Burada bağlantı sorunsuz çalışıp çalışmadığını kontrol ettik
        except Exception as conn_error:
            messages.error(request, f"SMTP bağlantısı başarısız oldu: {conn_error}")
            return HttpResponseRedirect(request.path)

        success_count = 0
        failure_count = 0
        obj = queryset

        if len(queryset) > 1:
            messages.error(message="Sadece bir konu seçebilirsiniz!", request=request)
            return HttpResponseRedirect(request.path)
        elif len(Subscriber.objects.all()) == 0:
            messages.error(message="Henüz kimse abone olmadığı için e-posta gönderilmedi!", request=request)
            return HttpResponseRedirect(request.path)
        else:
            obj = queryset[0]

        for subscriber in Subscriber.objects.all():

            try:

                template_name = os.path.join(BASE_DIR, "templates", "send_email", "news.html")
                template = get_template(template_name)
                context = {'obj': obj, 'unsubscribe_email': subscriber.email, 'neumorphism_site': site}
                html_content = template.render(context)
                body = HttpResponse(html_content).content.decode("utf-8")

                msg = EmailMultiAlternatives(
                    subject=obj.title,
                    body=body,
                    from_email=site.email,
                    to=[subscriber.email],
                )

                msg.content_subtype = "html"
                msg.send()
                success_count += 1

            except SMTPAuthenticationError as smtp_error:  # Özel olarak SMTPAuthenticationError için
                messages.error(request, f"Giriş yetkilendirme hatası: {smtp_error}")
                failure_count += 1
                break

            except Exception as e:
                messages.error(request, f"{subscriber.email} adresine e-posta gönderilemedi: {str(e)}")
                failure_count += 1

        if success_count:
            messages.success(request, f"{success_count} aboneye başarıyla e-posta gönderildi.")
        if failure_count:
            messages.warning(request, f"{failure_count} e-posta gönderilemedi.")

        try:
            connection.close()  # Bağlantıyı kapatmak önemli!
        except Exception as e:
            messages.error(request, f"SMTP bağlantısı kapatılamadı: {e}")


@admin.register(PortfolioCategory)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',)

    def has_module_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        return super().save_model(request, obj, form, change)


class PortFolioAddContentModelAdmin(admin.StackedInline):
    model = PortFolioAddContentModel
    extra = 0
    classes = ['collapse']


@admin.register(Portfolio)
class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'title', 'created')
    inlines = [PortFolioAddContentModelAdmin]


class ArticleTagsAdmin(admin.StackedInline):
    model = ArticleTags
    extra = 0
    classes = ['collapse']


class ArticleCommentAdmin(admin.StackedInline):
    model = ArticleComment
    extra = 0
    classes = ['collapse']


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'created_at')
    search_fields = ['title', 'author__username']
    list_filter = ('status', 'created_at')
    list_editable = ('status',)
    inlines = [ArticleCommentAdmin, ArticleTagsAdmin]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

    def has_module_permission(self, request):
        return False
