from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Employee
from .forms import UserRegisterForm

class UserAdmin(BaseUserAdmin):
    add_form = UserRegisterForm
    
    list_display = ('name','username','email','is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields':('username','email','password')}),
        ('Permissions',{'fields':('is_admin','is_staff','is_superuser')})
    )
    
    search_fields = ('name','username', 'email')
    ordering = ('name','username','email')
    
    filter_horizontal = ()
    

admin.site.register(Employee, UserAdmin)
admin.site.unregister(Group)

