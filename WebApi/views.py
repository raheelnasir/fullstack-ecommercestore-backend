from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *
from django.utils import timezone

class ProductManager(APIView):
    def get(self, request):
        try:
            products = Products.objects.prefetch_related('likes_received', 'reviews_received').all()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OrderDetailView(APIView):
    def get(self, request, id):
        try:
            order = OrderDetail.objects.prefetch_related('eachproductdetail').get(pk=id)
        except OrderDetail.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
class OrderCreateView(APIView):
     def post(self, request, format=None):
        serializer = OrderDetailSerializer(data=request.data)
        print("hi")
        if serializer.is_valid():
            # Save the order
            order = serializer.save() 
            print(1)
            each_product_details_data = request.data.get('eachproductdetail', []) 
            for product_data in each_product_details_data:
                product_id = product_data['id'] 
                print(2)
                try:
                    product_instance = Products.objects.get(pk=product_id)
                    EachProductDetail.objects.create(
                        orderid=order,
                        product=product_instance,
                        quantity=product_data['quantity']
                    )
                    print(3)
                except Products.DoesNotExist:
                    return Response(
                        {"error": f"Product with id {product_id} does not exist."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(5)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeManager(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            product = Products.objects.get(id=id)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        # Check if the user has already liked the product
        like, created = Likes.objects.get_or_create(user=user, product=product)

        if created:
            response_data = {"message": f"You liked {product.name}"}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            response_data = {"message": f"You unliked {product.name}"}
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        
class ReviewManager(APIView):
    def delete(self,request,id):
        user = request.user   
        
        review = Reviews.objects.get(pk=id)
        print(review)
        if review is not None and review.user == user:
            review.delete()
            print("Deleted")
            return Response("DELETED")
        else:
            print("Not deleted")   
            return Response("NOT DELETED")
        
    def post(self,request,id):
        user = request.user   
        comment = request.data.get("comments")
        product = Products.objects.get(pk=id)
        
        if product is not None and comment is not None and user is not None:
            rev = Reviews.objects.create(user=user,product=product,comments=comment)
            review = ReviewSerializer(rev)
            return  Response(review.data)
        else:
            return Response("INVALID")   
 
    def patch(self, request, pk):
        try:
            review = Reviews.objects.get(pk=pk)
        except Reviews.DoesNotExist:
            return Response({"detail": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

        if review.user != request.user:
            return Response({"detail": "You do not have permission to edit this review"}, status=status.HTTP_403_FORBIDDEN)

        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
