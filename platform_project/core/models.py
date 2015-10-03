from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Platform(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Store(models.Model):
    name = models.CharField(max_length=75)
    platform = models.ForeignKey(Platform, related_name='stores')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    store = models.ForeignKey(Store, related_name='products')

    def __str__(self):
        return self.name
