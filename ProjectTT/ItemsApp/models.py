import pathlib
import uuid

from django.db import models
from decimal import Decimal 
from django.core.validators import MinValueValidator
from django.urls import reverse

# Create your models here.

#Adding extra source models for certain fields of "ModelProduct" to support scalability
    
class ModelCategory(models.Model):
    sourceCategory = models.CharField(max_length = 20, unique = True)

    class Meta:
        ordering = ["sourceCategory"]

    def __str__(self):
        return f"{self.sourceCategory}"
    
class ModelManufacturer(models.Model):
    sourceManufacturer = models.CharField(max_length = 30, unique = True)

    class Meta:
        ordering = ["sourceManufacturer"]

    def __str__(self):
        return f"{self.sourceManufacturer}"

#Using 'pathlib'
def product_image_upload_handler(instance, filename): #upload files to seperate DIR so that same-name files dont overlap/overwrite eachother
    fpath = pathlib.Path(filename)
    newFileName = str(uuid.uuid1()) #uuid1 is uuid with time/datetime
    return f"productImages/{newFileName}{fpath.suffix}" #{fpath.suffix} includes file-name ending suffixes like .png and .jpg

class ModelProduct(models.Model):   #inherits from default python class "Model"
    name = models.CharField(max_length = 60, unique = True)
    image = models.ImageField(blank=True, null=True, upload_to=product_image_upload_handler)
    description = models.TextField(blank = True, null = True)
    category = models.ForeignKey(ModelCategory, on_delete=models.SET_NULL, blank = True, null = True)
    release_date = models.DateField(blank=True, null = True)
    current_stock = models.PositiveIntegerField(default=0)
    manufacturer = models.ForeignKey(ModelManufacturer, on_delete=models.SET_NULL, blank = True, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 8, validators=[MinValueValidator(Decimal('0.01'))]) #imported validator to keep values Positive and Decimal
    featured_status = models.BooleanField(blank = True, null = True, default=False)
    featured_promo_overlay = models.ImageField(blank=True, null=True)


