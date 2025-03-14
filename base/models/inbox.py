from django.db import models


class Inbox(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ad Soyad')
    email = models.EmailField()
    subject = models.CharField(max_length=100, verbose_name='Konu')
    message = models.TextField(verbose_name='Mesaj')
    is_read = models.BooleanField(default=False, verbose_name='Okundu ?', editable=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Gönderme Tarihi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "İletişim"
