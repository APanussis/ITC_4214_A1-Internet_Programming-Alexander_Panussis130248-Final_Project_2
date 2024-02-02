from django.db import models
from decimal import Decimal 
from django.core.validators import MinValueValidator

# Create your models here.

class ModelUser(models.Model):
    name = models.CharField(max_length = 60, unique = True)
    email = models.EmailField(blank=False, null = False, unique = True)
    image = models.ImageField(blank=True, null=True, upload_to="userImages/")
    description = models.TextField(blank = True, null = True)
    date_joined = models.DateField(blank=False, null = False)
    age = models.PositiveIntegerField(blank = True, null = True, default=0)
    orders_made = models.PositiveIntegerField(default=0)