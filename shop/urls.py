from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('urunler/', ProductListView.as_view(), name='product_list'),
    path('urunler/<pk>/<category>/<slug>/', ProductDetailView.as_view(), name='product_detail'),
]
