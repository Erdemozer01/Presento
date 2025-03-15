from django.db import models

# Create your models here.

from autoslug import AutoSlugField
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Kategori')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    slug = AutoSlugField(populate_from='name', unique_with='created', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ürün Kategorisi'
        verbose_name_plural = 'Ürün Kategorisi'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Ürün Kategorisi',
                                 related_name='categories')
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=100, verbose_name='Ürün adı')
    content = CKEditor5Field(config_name='extends', verbose_name='İçerik')

    stock = models.PositiveIntegerField(default=0, verbose_name='Stok')
    price = models.FloatField(verbose_name='Fiyat')
    ordered = models.PositiveIntegerField(verbose_name='Satış adeti', default=0, db_index=True)
    is_stock = models.BooleanField(default=True, verbose_name='Stokta var mı ?')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    updated = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def save(self, *args, **kwargs):
        if self.stock >= 0:
            self.is_stock = True
        return super().save(*args, **kwargs)