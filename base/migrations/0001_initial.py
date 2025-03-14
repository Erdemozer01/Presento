# Generated by Django 5.1.5 on 2025-01-18 01:06

import autoslug.fields
import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tab Panel')),
                ('icon', models.CharField(help_text="Ör : binoculars <h6>İngilizce yazın. Daha fazlası için <a href='https://icons.getbootstrap.com/' target='_blank'>Tıklayın</a></h6>", max_length=50, verbose_name='Icon ADI')),
            ],
            options={
                'verbose_name': 'Hakkımızda Kategori',
                'verbose_name_plural': 'Hakkımızda Kategori',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anasayfa', max_length=100, unique=True, verbose_name='Site Adı')),
                ('email', models.EmailField(blank=True, help_text='Email göndermek için kullanılacak', max_length=254, verbose_name='Email')),
                ('email_password', models.CharField(blank=True, max_length=100, verbose_name='Email şifresi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturuldu')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Düzenlendi')),
            ],
            options={
                'verbose_name': 'Ayar',
                'verbose_name_plural': 'Ayarlar',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad Soyad')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100, verbose_name='Konu')),
                ('message', models.TextField(verbose_name='Mesaj')),
                ('is_read', models.BooleanField(default=False, editable=False, verbose_name='Okundu ?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Gönderme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'İletişim',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Abone',
                'verbose_name_plural': 'Aboneler',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Hero/', verbose_name='Foto')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='İçerik')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('video', models.URLField(blank=True, verbose_name='Video URL')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heros', to='base.home')),
            ],
            options={
                'verbose_name': 'Başlık',
                'verbose_name_plural': 'Başlık',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Soru')),
                ('answer', models.TextField(verbose_name='Cevap')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frequently', to='base.home')),
            ],
            options={
                'verbose_name': 'Sıkça Sorulan Sorular',
                'verbose_name_plural': 'Sıkça Sorulan Sorular',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('address', models.CharField(max_length=100, verbose_name='Adres')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefon')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='base.home')),
            ],
            options={
                'verbose_name': 'İletişim Bilgileri',
                'verbose_name_plural': 'İletişim Bilgileri',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad')),
                ('logo', models.ImageField(upload_to='Clients/', verbose_name='Logo')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='base.home')),
            ],
            options={
                'verbose_name': 'Müşteri - Sponsor',
                'verbose_name_plural': 'Müşteri - Sponsor',
            },
        ),
        migrations.CreateModel(
            name='AboutTab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='İçerik')),
                ('image', models.ImageField(upload_to='About/', verbose_name='Hakkımızda Görüntüsü')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.aboutcategory')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='base.home')),
            ],
            options={
                'verbose_name': 'Hakkımızda',
                'verbose_name_plural': 'Hakkımızda',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Hizmet Adı')),
                ('icon', models.CharField(help_text="Ör : binoculars <h6>İngilizce yazın. Daha fazlası için <a href='https://icons.getbootstrap.com/' target='_blank'>Tıklayın</a></h6>", max_length=50, verbose_name='Icon ADI')),
                ('image', models.ImageField(upload_to='Services/', verbose_name='Foto')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(help_text='Hizmetinizi detaylı açıklayın', verbose_name='Hizmet İçeriği')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='base.home')),
            ],
            options={
                'verbose_name': 'Hizmetlerimiz',
                'verbose_name_plural': 'Hizmetlerimiz',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Teams/', verbose_name='Foto')),
                ('name', models.CharField(max_length=100, verbose_name='Ad Soyad')),
                ('department', models.CharField(max_length=100, verbose_name='Bölüm')),
                ('twitter', models.CharField(blank=True, max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=100, verbose_name='Instagram')),
                ('facebook', models.CharField(blank=True, max_length=100, verbose_name='Facebook')),
                ('linkedin', models.CharField(blank=True, max_length=100, verbose_name='Linkedin')),
                ('github', models.CharField(blank=True, max_length=100, verbose_name='Github')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='base.home')),
            ],
            options={
                'verbose_name': 'Ekip Arkadaşlarımız',
                'verbose_name_plural': 'Ekip Arkadaşlarımız',
                'ordering': ['-created'],
            },
        ),
    ]
