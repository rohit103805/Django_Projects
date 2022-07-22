from django.db import models

# Create your models here.

class Suggested_Places(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='suggested_pics')
    coord_x = models.DecimalField(max_digits=9, decimal_places=4)
    coord_y = models.DecimalField(max_digits=9, decimal_places=4)

class Hotels(models.Model):
   name = models.CharField(max_length=100)
   coord_x = models.DecimalField(max_digits=9, decimal_places=6)
   coord_y = models.DecimalField(max_digits=9, decimal_places=6)
   price = models.IntegerField()
   located = models.CharField(max_length=100)
   address = models.CharField(max_length=2000)

class Booking(models.Model):
    user=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    hotel_id=models.CharField(max_length=20)
    price=models.IntegerField()