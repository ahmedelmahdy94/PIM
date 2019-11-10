from django.db import models
import uuid


# Create your models here.


class Category(models.Model):
    CategoryID = models.UUIDField(
        auto_created=True, default=uuid.uuid4, unique=True, primary_key=True)
    CategoryName = models.CharField(max_length=50)
    CategoryActive = models.BooleanField(default=True)


class Product(models.Model):
    ProductID = models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True, primary_key=True)
    ProductCode = models.CharField(max_length=50)
    ProductName = models.CharField(max_length=50)
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ProductAvailableQuantity = models.IntegerField()
    ProductCategoryID = models.ManyToManyField('category')
    ProductActive = models.BooleanField(default=True)
