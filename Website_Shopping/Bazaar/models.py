from django.db import models

# Create your models here.

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='product_pics')
    desc = models.TextField()
    price = models.IntegerField()
    free_delivery = models.BooleanField(default=False)

class FootWear(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='product_pics')
    desc = models.TextField()
    price = models.IntegerField()
    free_delivery = models.BooleanField(default=False)

class SkinCare(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='product_pics')
    desc = models.TextField()
    price = models.IntegerField()
    free_delivery = models.BooleanField(default=False)

class Order(models.Model):
    user=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    prod_id=models.CharField(max_length=10)
    price=models.IntegerField()
    delivery_address=models.TextField()
    razorpay_order_id=models.TextField()
    razorpay_payment_id=models.TextField()
    razorpay_signature=models.TextField()
