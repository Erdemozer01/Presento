from django.contrib.sitemaps import Sitemap

from .models import Product

class MySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.all()  # Modeldeki tüm nesneleri döndürür

    def location(self, obj):
        return f'/urunler/{obj.pk}/{obj.category}/{obj.slug}/'
