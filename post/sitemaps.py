from django.contrib.sitemaps import Sitemap

from .models import ArticleModel

class MySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ArticleModel.objects.all()  # Modeldeki tüm nesneleri döndürür

    def location(self, obj):
        return '/my-model-url/%s/' % obj.pk  # Her nesnenin URL'sini belirtir
