from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart', verbose_name='Müşteri')
    cart_number = models.CharField(max_length=100, verbose_name='Sepet ID')
    total = models.FloatField(default=0)
    is_ordered = models.BooleanField(default=False, verbose_name='Sipariş verildi mi ?')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.user.username + ' ' + self.cart_number

    class Meta:
        verbose_name = 'Sepet'
        verbose_name_plural = 'Sepetler'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item', verbose_name='Sepet')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_item', verbose_name='Ürün')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Miktar')
    sub_total = models.FloatField(default=0, verbose_name='Ara Toplam')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Sepetteki Ürün'
        verbose_name_plural = 'Sepetteki Ürünler'


class Payment(models.Model):
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.status}"
