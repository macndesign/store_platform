from __future__ import unicode_literals, absolute_import
from django.shortcuts import render
from rest_framework import viewsets
from core.models import Platform, Store, Product
from core.serializers import PlatformSerializer, StoreSerializer, ProductSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
