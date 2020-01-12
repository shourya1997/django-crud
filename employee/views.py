from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics


from .serializers import EmployeeSerializer
from .models import Employee 

# permission_classes = (IsAuthenticated, )



