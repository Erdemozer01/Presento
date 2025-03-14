from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


def upload_to(instance, filename):
    try:
        return f'Portfolios/{instance.category.user}/{instance.title}/{filename}'
    except:
        return f'Portfolios/{instance.portfolio.category.user}/{instance.portfolio.title}/contents/{filename}'


class PortfolioCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Oluşturan Kullanıcı', editable=False)
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Kategori adı')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.title()
        return super(PortfolioCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class Portfolio(models.Model):
    name = models.CharField(max_length=100, verbose_name='Hazırlayan', help_text='Hazırlayan adı soyad yada proje adı', unique=True, db_index=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, verbose_name='Kategori:')
    title = models.CharField(max_length=100, verbose_name="Başlık")
    image = models.ImageField(upload_to=upload_to, verbose_name="Foto", max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


class PortFolioAddContentModel(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='portfolio')
    title = models.CharField(max_length=200, verbose_name="Başlık")
    image = models.ImageField(upload_to=upload_to, verbose_name="Foto", max_length=500)
    content = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Portfolio içerik"
        verbose_name_plural = "Portfolio içerik"
