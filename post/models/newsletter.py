from django.db import models


class NewsLetterModel(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")

    created = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Bülten'
        verbose_name_plural = 'Bülten'
