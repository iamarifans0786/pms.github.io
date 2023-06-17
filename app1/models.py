from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class electronic_items_earphones(models.Model):
    product_name=models.CharField(max_length=100)
    description=HTMLField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stocks=models.IntegerField()
    color=models.CharField(max_length=20)

    def __str__(self):
        return str(self.product_name)
     
class electronic_items_mobiles(models.Model):
    product_name=models.CharField(max_length=100)
    description=HTMLField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stocks=models.IntegerField()
    color=models.CharField(max_length=20)

    def __str__(self):
        return str(self.product_name)    
    

class electronic_items_watch(models.Model):
    product_name=models.CharField(max_length=100)
    description=HTMLField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stocks=models.IntegerField()
    color=models.CharField(max_length=20)

    def __str__(self):
        return str(self.product_name)        