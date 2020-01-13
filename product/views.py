from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .serializers import ProductSerializer
from .models import Product 

# TODO: Custom Product login

# Add Product 
# post
class ProductCreateView(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# View all Product
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# View, Update, Delete Product instance
# get, put, patch, delete
class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    queryset = Product.objects.all()