from django import forms

from .models import ModelProduct

class FormProductCreate(forms.ModelForm):
    class Meta:
        model = ModelProduct
        fields = [
            'name',
            'image',
            'description',
            'category',
            'releaseDate',
            'currentStock',
            'manufacturer',
            'price',
            'featuredStatus',
            'featuredPromoOverlay',
        ]

# # # # # # #
# REFERENCE #
# # # # # # #                         
# class ModelProduct(models.Model):   #inherits from default python class "Model"
#     name = models.CharField(max_length = 60, unique = True)
#     image = models.ImageField(blank=True, null=True, upload_to="productImages/")
#     description = models.TextField(blank = True, null = True)
#     category = models.CharField(max_length = 20)
#     releaseDate = models.DateField(blank=True, null = True)
#     currentStock = models.PositiveIntegerField(default=0)
#     manufacturer = models.CharField(max_length = 30)
#     price = models.DecimalField(decimal_places = 2, max_digits = 8)
#     featuredStatus = models.BooleanField(blank = True, null = True, default=False)
#     featuredPromoOverlay = models.ImageField(blank=True, null=True)