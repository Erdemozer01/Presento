from django.contrib import admin
from .models import Product,ProductCategory

# Register your models here.


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock', 'price', 'ordered', 'is_stock')
    list_filter = ('is_stock',)
    search_fields = ('name', 'category__name')
    search_help_text = 'Başlık yada Kategori adı'
    list_editable = ('price', 'stock',)
    readonly_fields = ('created', 'is_stock', 'ordered')