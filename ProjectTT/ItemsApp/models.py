from django.db import models

# Create your models here.

class ModelProduct(models.Model):   #inherits from default python class "Model"
    name = models.CharField(max_length = 60, unique = True)
    image = models.ImageField(upload_to="productImages/")
    description = models.TextField(blank = True, null = True)
    category = models.CharField(max_length = 20)
    releaseDate = models.DateField(blank=True, null = True)
    currentStock = models.PositiveIntegerField(default=0)
    manufacturer = models.CharField(max_length = 30)
    price = models.DecimalField(decimal_places = 2, max_digits = 8)
    featuredStatus = models.BooleanField(blank = True, null = True, default=False)
    featuredPromoOverlay = models.ImageField(blank=True, null=True)