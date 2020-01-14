from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from employee.views import EmployeeCreateView, EmployeeListView, EmployeeUpdateView

app_name = 'employee'

urlpatterns = [
    path('e/create', EmployeeCreateView.as_view(), name='test'),
    path('e/list', EmployeeListView.as_view(), name='list'),
    path('e/update/<int:pk>', EmployeeUpdateView.as_view(), name='list'),
    path('e/api/token', obtain_auth_token, name='obtain-token'),
    
]