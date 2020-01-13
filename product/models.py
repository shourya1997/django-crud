from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=120)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name