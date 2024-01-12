from django.db import models

# Create your models here.
class Product(models.Model):
    pcode=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    mfd=models.CharField(max_length=100)
    exp=models.CharField(max_length=20)
    prod_count=models.IntegerField(default=0)


    def __str__(self):
        return self.pname


class ProductDiscount(models.Model):
    prodname=models.CharField(max_length=100)
    pdiscount=models.CharField(max_length=200)


    def __str__(self):
        return self.pname


class Bestseller(models.Model):
    pcode = models.IntegerField()
    pname = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    mfd = models.CharField(max_length=100)
    exp = models.CharField(max_length=20)
    prod_count = models.IntegerField(default=0)

    def __str__(self):
        return self.pname