from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    e_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name