from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Food_Donation(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    description=models.CharField(max_length=200)

class Food_Section(models.Model):
    rating=models.CharField(max_length=10)
    food_img=models.ImageField(default=False,upload_to='static/pictures')
    food_id=models.CharField(max_length=10)
    food_type=models.CharField(max_length=100)
    food_price=models.IntegerField(max_length=10)
    
class Contact(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(null=True)
    user_mob=models.IntegerField(max_length=10)
    user_desc=models.CharField(max_length=500)

class Address(models.Model):
    address=models.CharField(max_length=1000)
    email=models.EmailField(null=True)
    mob=models.IntegerField(max_length=10,default=9999999999)
    pin=models.IntegerField(max_length=6,null=True)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=100,null=True)

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    food_name=models.CharField(max_length=100)
    order_date = models.DateField(default=timezone.now)
    count=models.IntegerField()
    status=models.CharField(max_length=30,choices=[("Pending","Pending"),("Order Accept","Order Accept"),("Delivered","Delivered")],default="Pending")


class Payment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    order_id=models.CharField(max_length=50,null=False)
    payment_id=models.CharField(max_length=50)
    amount=models.IntegerField(default=0)
    ordered_items=models.ManyToManyField(Order)
    status=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    

