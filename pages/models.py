from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    ex_price = models.IntegerField()
    rating = models.IntegerField()
    sale = models.BooleanField()
    pack = models.BooleanField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='')