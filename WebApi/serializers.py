from django.contrib.auth.models import User  # Import the User model
from rest_framework import serializers
from .models import *


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    

    class Meta:
        model = Reviews
        fields = ['id', 'comments', 'user', 'product', 'user_name']  # Include 'user_name' in the fields
    
    def get_user_name(self, obj):
        user = User.objects.get(id=obj.user_id)  # Assuming user_id is the field containing the user's ID in the Review model
        return user.username
    
class ProductsSerializer(serializers.ModelSerializer):
    likes_received = LikesSerializer(many=True, read_only=True)
    reviews_received = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'image','description', 'price', 'likes_received', 'reviews_received']

class EachProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = EachProductDetail
        fields = ['id', 'orderid', 'product', 'quantity']

class OrderDetailSerializer(serializers.ModelSerializer):
    eachproductdetail = EachProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = OrderDetail
        fields = ['id', 'user', 'ordertime', 'totalprice', 'address','eachproductdetail']
   
             




