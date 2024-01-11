from django.db import models

# Create your models here.
class Product(models.Model):
    pcode=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=4)
    mfd=models.DateField()
    exp=models.DateField()
    prod_count=models.IntegerField()


    def __str__(self):
        return self.name


class ProductDiscount(models.Model):
    prodname=models.CharField(max_length=100)
    pdiscount=models.CharField(max_length=200)


    def __str__(self):
        return self.name


