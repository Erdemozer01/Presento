from django.db import models
from autoslug.fields import AutoSlugField
from django_ckeditor_5.fields import CKEditor5Field


def cover_upload_to(instance, filename):
    return 'article/{0}/cover/{1}'.format(instance.title[:50], filename).replace(' ', '_')


def images_upload_to(instance, filename):
    return 'article/{0}/img/{1}'.format(instance.article.title[:50], filename)


class ArticleCategory(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Kategori adı')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=ArticleModel.Status.PUBLISHED)


class ArticleModel(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Taslak'
        PUBLISHED = 'PB', 'Yayınlandı'

    category = models.ForeignKey(ArticleCategory, on_delete=models.PROTECT, verbose_name='Kategori', related_name='articles')

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='post', editable=False,
                               verbose_name='Yazar')
    cover = models.ImageField(upload_to=cover_upload_to, verbose_name='Gönderi Fotosu', max_length=255)

    title = models.CharField(max_length=500, verbose_name="Başlık", unique=True, db_index=True)

    content = CKEditor5Field(verbose_name="İçerik", config_name="extends")

    slug = AutoSlugField(populate_from='title', unique_with='category')

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT,
                              verbose_name='Durum')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturuldu")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellendi")

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'article_model'
        verbose_name = 'Makale'
        verbose_name_plural = 'Makale'


class ArticleComment(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, verbose_name='Makale', related_name='comments')

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments', editable=False,
                               verbose_name='Yorumcu')

    comment = models.TextField(verbose_name="Yorum")

    report_count = models.IntegerField(default=0, verbose_name="Kötüye kullanım sayısı")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + ' ' + self.created_at.strftime('%d/%m/%Y') + '\n\t' + self.comment

    class Meta:
        db_table = 'article_comment'
        ordering = ['-created_at']
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"


class ArticleTags(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='article_tags')
    tags = models.CharField(max_length=100, verbose_name="Etiketler")

    def __str__(self):
        return self.tags

    def save(self, *args, **kwargs):
        self.tags = self.tags.lower()
        return super(ArticleTags, self).save(*args, **kwargs)

    class Meta:
        db_table = 'article_tags'
        verbose_name = 'Makale Etiketleri'
        verbose_name_plural = 'Makale Etiketleri'
