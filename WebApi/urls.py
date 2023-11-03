from django.urls import path,include
from WebApi import urls
from .views import *
urlpatterns = [
    path("api/products/", ProductManager.as_view(), name="PRODUCT"),
    path('api/orders/post/', OrderCreateView.as_view(), name='order-create'),  # Add this line
    path("api/likes/<int:id>/",LikeManager.as_view(),name="LIKE PRODUCT"),
    path("api/del_review/<int:id>/",ReviewManager.as_view(), name="Delete Review"),
    path("api/post_review/<int:id>/",ReviewManager.as_view(), name="Post Review"),
    path('api/edit_review/<int:pk>/', ReviewManager.as_view(), name='edit-review'),
]

