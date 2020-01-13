from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics

from .serializers import EmployeeSerializer
from .models import Employee 

# TODO: Employee login

# Add employee 
# post
class EmployeeCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

# View all employee
class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

# View, Update, Delete employee instance
# get, put, patch, delete
class EmployeeUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


