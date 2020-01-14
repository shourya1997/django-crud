from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from employee.views import EmployeeCreateView, EmployeeListView, EmployeeUpdateView, login_view, register_view, logout_view

app_name = 'employee'

urlpatterns = [
    path('e/create', EmployeeCreateView.as_view(), name='test'),
    path('e/list', EmployeeListView.as_view(), name='list'),
    path('e/update/<int:pk>', EmployeeUpdateView.as_view(), name='list'),
    path('e/api/token', obtain_auth_token, name='obtain-token'),
<<<<<<< HEAD
    
=======
    path('e/login', login_view, name='login'),
    path('e/logout', logout_view, name='logout'),
    path('e/register', register_view, name='register'),

>>>>>>> custom-user
]