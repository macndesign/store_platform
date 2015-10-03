from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from core.models import Platform, Store, Product


class PlatformSerializer(serializers.ModelSerializer):
    stores = serializers.HyperlinkedRelatedField(view_name='store-detail', many=True, read_only=True)

    class Meta:
        model = Platform
        fields = ('url', 'name', 'stores')


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(view_name='product-detail', many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('url', 'name', 'platform', 'products')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'name', 'price', 'store')
