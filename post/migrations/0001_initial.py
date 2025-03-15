# Generated by Django 5.1.5 on 2025-03-15 18:53

import autoslug.fields
import django.db.models.deletion
import django_ckeditor_5.fields
import post.models.article
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Kategori adı')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='NewsLetterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news/')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')),
            ],
            options={
                'verbose_name': 'Bülten',
                'verbose_name_plural': 'Bülten',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Kategori')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name', unique_with=('created',))),
            ],
            options={
                'verbose_name': 'Ürün Kategorisi',
                'verbose_name_plural': 'Ürün Kategorisi',
            },
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(max_length=255, upload_to=post.models.article.cover_upload_to, verbose_name='Gönderi Fotosu')),
                ('title', models.CharField(db_index=True, max_length=500, unique=True, verbose_name='Başlık')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='İçerik')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('category',))),
                ('status', models.CharField(choices=[('DF', 'Taslak'), ('PB', 'Yayınlandı')], default='DF', max_length=2, verbose_name='Durum')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturuldu')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellendi')),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='post.articlecategory', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Makale',
                'verbose_name_plural': 'Makale',
                'db_table': 'article_model',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Yorum')),
                ('report_count', models.IntegerField(default=0, verbose_name='Kötüye kullanım sayısı')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Yorumcu')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.articlemodel', verbose_name='Makale')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'db_table': 'article_comment',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=100, verbose_name='Etiketler')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_tags', to='post.articlemodel')),
            ],
            options={
                'verbose_name': 'Makale Etiketleri',
                'verbose_name_plural': 'Makale Etiketleri',
                'db_table': 'article_tags',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
                ('name', models.CharField(max_length=100, verbose_name='Ürün adı')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='İçerik')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stok')),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('ordered', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Satış adeti')),
                ('is_stock', models.BooleanField(default=True, verbose_name='Stokta var mı ?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='post.productcategory', verbose_name='Ürün Kategorisi')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]
