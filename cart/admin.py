from django.contrib import admin
from .models import Product, Cart, CartItem, Payment


# Register your models here.


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    classes = ['collapse']
    readonly_fields = ('product', 'sub_total', 'quantity')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'user__last_name', 'user__email', 'total', 'is_ordered', 'created',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    search_help_text = 'Ad, soyad yada Email adresine göre arayın.'
    readonly_fields = ('cart_number', 'is_ordered', 'user', 'total', 'created')
    list_filter = ('is_ordered', 'created',)
    inlines = [CartItemInline]

    def has_add_permission(self, request):
        return False