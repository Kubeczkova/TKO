from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from shop.serializers import ProductSerializer, OrderSerializer

from shop.models import Product


# Create your views here.

class LoadProductsView(ListAPIView):
    serializer_class = ProductSerializer
    template_name = 'shop/shop.html'

    def get_queryset(self):
        return Product.objects.all()


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer

