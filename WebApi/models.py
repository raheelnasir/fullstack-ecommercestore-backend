from django.db import models
from django.contrib.auth.models import User


class TemporaryModel(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,default="0")
    email=models.EmailField(max_length=50,default="@")
    address = models.CharField(max_length=999,default="PINDI BOI")
    token = models.CharField(max_length=10, default="0")
    
class UserProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,default="0")
    email=models.EmailField(max_length=50,default="@")
    address = models.CharField(max_length=999,default="PINDI BOI")
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}"



class Products(models.Model):
    name = models.CharField(max_length=100, default="Product")
    image = models.ImageField(upload_to='product_images/', default="path/to/default_image.jpg")
    description = models.CharField(max_length=500, default="Product description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_given')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='likes_received')

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_given')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews_received')
    comments = models.CharField(max_length=10000,default="Review Done")

class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordertime = models.DateTimeField(auto_now_add=True)
    totalprice= models.DecimalField(decimal_places=2, default=0.0,max_digits=10)
    address = models.CharField(max_length=999, default= "PINDI")
   
class EachProductDetail(models.Model):
    orderid = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, related_name='eachproductdetail')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
   