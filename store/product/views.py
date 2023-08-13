from django.shortcuts import render
from rest_framework import generics
from .models import ProductCategory, Product
from .serializers import ProductCategorySerializer, ProductSerializer
from rest_framework import filters

class ProductCategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class CategorySearchView(generics.ListAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer