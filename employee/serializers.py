from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'username','name', 'email', 'e_id', 'is_admin', 'is_staff'
        )