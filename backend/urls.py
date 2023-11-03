from django.contrib import admin
from django.urls import path, include
from WebApi import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),  # Include the URLs from the WebApi app
]
