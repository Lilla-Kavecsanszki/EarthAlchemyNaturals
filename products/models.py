from django.db import models
from herbs.models import Herb

# Category model


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# SkinType model
class SkinType(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product model
class Product(models.Model):
    name = models.CharField(max_length=250)
    star_ingredients = models.ForeignKey(
        'herbs.Herb', null=True, on_delete=models.SET_NULL)
    milliliter = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    sku = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    member_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    skin_types = models.ManyToManyField('SkinType')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
