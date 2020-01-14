from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

class EmployeeManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have email address')
        
        user = self.model(username=username,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Employee(AbstractUser):
    username = models.CharField(max_length=100,
                                validators = [RegexValidator(regex=USERNAME_REGEX,
                                                             message='Username must be alphanumeric',
                                                             code='invalid_username')],
                                unique=True)
    
    email = models.EmailField(max_length=255,
                              unique=True,
                              verbose_name='email address')
    
    name = models.CharField(max_length=100, verbose_name='name')
    e_id = models.AutoField(primary_key=True)
    
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))    
    
    is_admin = models.BooleanField(choices=BOOL_CHOICES, default=False)
    is_staff = models.BooleanField(choices=BOOL_CHOICES, default=False)
    is_superuser = models.BooleanField(choices=BOOL_CHOICES, default=False)
    
    objects = EmployeeManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

# create token when creating profile
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     e_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name