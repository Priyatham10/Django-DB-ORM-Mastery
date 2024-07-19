import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    slug = models.SlugField() # URL friendly string. Derived from another variable for example name here
    description = models.TextField() # For larger texts we use TextField in contrast to CharField
    is_digital = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

class ProductLine(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField()
    is_active = models.BooleanField()
    order = models.IntegerField()
    weight = models.FloatField()

class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField()

class SeasonalEvents(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100)
