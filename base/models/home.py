from autoslug import AutoSlugField
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Home(models.Model):
    name = models.CharField(max_length=100, default="Anasayfa", unique=True, verbose_name='Site Adı')
    email = models.EmailField(verbose_name='Email', blank=True, help_text='Email göndermek için kullanılacak')
    email_password = models.CharField(verbose_name='Email şifresi', max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturuldu')
    updated = models.DateTimeField(auto_now=True, verbose_name='Düzenlendi')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'


class MetaTags(models.Model):
    meta_type = [
        ('genel', 'genel'),
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('google', 'google'),
        ('canonical', 'canonical'),
    ]
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='meta_tags')
    tag = models.CharField(verbose_name='Tag türü', max_length=100, choices=meta_type)
    name = models.CharField(max_length=50, verbose_name='Tag Adı')
    content = models.TextField(verbose_name='Tag İçeriği')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Meta Tag'
        verbose_name_plural = 'Meta Taglar'


class Hero(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='heros')

    image = models.ImageField(upload_to='Hero/', verbose_name="Foto")
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = CKEditor5Field(config_name="extends", verbose_name="İçerik")
    slug = AutoSlugField(populate_from='title')
    video = models.URLField(verbose_name='Video URL', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Başlık'
        verbose_name_plural = 'Başlık'


class Clients(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='clients')
    name = models.CharField(max_length=100, verbose_name="Ad")
    logo = models.ImageField(verbose_name="Logo", upload_to="Clients/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Müşteri - Sponsor'
        verbose_name_plural = 'Müşteri - Sponsor'


class AboutCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tab Panel")
    icon = models.CharField(
        max_length=50, verbose_name="Icon ADI",
        help_text="Ör : binoculars <h6>İngilizce yazın. Daha fazlası için <a href='https://icons.getbootstrap.com/' target='_blank'>Tıklayın</a></h6>"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hakkımızda Kategori'
        verbose_name_plural = 'Hakkımızda Kategori'


class AboutTab(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='about')
    category = models.ForeignKey(AboutCategory, on_delete=models.CASCADE)

    content = CKEditor5Field(config_name="extends", verbose_name='İçerik')
    image = models.ImageField(verbose_name="Hakkımızda Görüntüsü", upload_to="About/")

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.title

    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = "Hakkımızda"


class Services(models.Model):
    class IconType(models.TextChoices):
        FONTAWESOME = 'fa', 'Fontawesome'
        BOOTSTRAP = 'bi', 'Bootstrap'

    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='services')

    title = models.CharField(max_length=100, verbose_name="Hizmet Adı")

    icon_type = models.CharField(verbose_name='İcon Türü', max_length=2, choices=IconType.choices,
                                 default=IconType.BOOTSTRAP,  help_text="<h6>Daha fazlası için, <a href='https://icons.getbootstrap.com/' target='_blank'>Bootstrap iconları</a>, <a href='https://fontawesome.com/search' target='_blank'>Fontawesome iconları</a></h6>")

    icon = models.CharField(
        max_length=50, verbose_name="Icon Sınıfı",
        help_text="Ör : bi bi-binoculars"
    )

    image = models.ImageField(upload_to='Services/', verbose_name="Foto")
    content = CKEditor5Field(config_name="extends", help_text="Hizmetinizi detaylı açıklayın",
                             verbose_name='Hizmet İçeriği')
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hizmetlerimiz'
        verbose_name_plural = 'Hizmetlerimiz'


class FrequentlyAskedQuestions(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='frequently')

    question = models.CharField(max_length=100, verbose_name='Soru')
    answer = models.TextField(verbose_name="Cevap")

    created = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Sıkça Sorulan Sorular'
        verbose_name_plural = 'Sıkça Sorulan Sorular'
        ordering = ['-created']


class Team(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='teams')

    image = models.ImageField(verbose_name="Foto", upload_to="Teams/")
    name = models.CharField(verbose_name="Ad Soyad", max_length=100)
    department = models.CharField(verbose_name="Bölüm", max_length=100)

    twitter = models.CharField(verbose_name="Twitter", max_length=100, blank=True)
    instagram = models.CharField(verbose_name="Instagram", max_length=100, blank=True)
    facebook = models.CharField(verbose_name="Facebook", max_length=100, blank=True)
    linkedin = models.CharField(verbose_name="Linkedin", max_length=100, blank=True)
    github = models.CharField(verbose_name="Github", max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = 'Ekip Arkadaşlarımız'
        verbose_name_plural = 'Ekip Arkadaşlarımız'


class Contact(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='contacts')

    email = models.EmailField(verbose_name="Email", max_length=100)
    address = models.CharField(verbose_name="Adres", max_length=100)
    phone = models.CharField(verbose_name="Telefon", max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'İletişim Bilgileri'

    class Meta:
        ordering = ['-created']
        verbose_name = 'İletişim Bilgileri'
        verbose_name_plural = 'İletişim Bilgileri'


class Subscriber(models.Model):
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Abone"
        verbose_name_plural = "Aboneler"


class SocialNetwork(models.Model):
    page = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='social_networks')
    name = models.CharField(verbose_name="Social Medya", max_length=100,
                            help_text="facebook, twitter, instagram, linkedin, github")
    url = models.URLField(verbose_name="Social Medya URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social Medya"
        verbose_name_plural = "Social Medya"
