from requests import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from inetshop.models import Product, Shop, Category
from inetshop.serializers import ProductSerializer, ShopSerializer
from django.shortcuts import render


class ProductView(APIView):

    def get(self, request, *args, **kwargs):
        Product.objects.create(name='Telephone', category=Category.objects.create(name='Телефон'), )
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(queryset, many=True)
        print(serializer_class.data)
        return Response(serializer_class)
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['title', 'description']
    # при необходимости добавьте параметры фильтрации


# class ShopView(APIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#     filter_backends = [SearchFilter, DjangoFilterBackend]
#     filterset_fields = ['products', ]
#     search_fields = ['products__title']





