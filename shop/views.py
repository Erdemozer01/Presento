from django.shortcuts import render
from .models import Product, ProductCategory

from django.views import generic


# Create your views here.


class ProductListView(generic.ListView):
    model = Product
    template_name = 'pages/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['pk'])
