from PIL import Image
from django import forms
from django.forms import SelectDateWidget
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import ModelProduct

class FormProductCreate(forms.ModelForm):
    class Meta:
        model = ModelProduct
        fields = [
            'name',
            'image',
            'description',
            'category',
            'release_date',
            'current_stock',
            'manufacturer',
            'price',
            'featured_status',
            'featured_promo_overlay',
        ]

class rFormProductCreate(forms.Form):
    name                    = forms.CharField(max_length = 60) 
    image                   = forms.ImageField(required=False) 
    description             = forms.CharField(widget=forms.Textarea)    #TextArea widget to give the user space to write something more than a single sentence.
    category                = forms.CharField(max_length = 20)
    release_date            = forms.DateField(                          #DateInput widget for convenience
                                    widget= forms.DateInput 
                                        (attrs=
                                            {                       
                                                'type':'date',
                                                'placeholder': 'Unknown Release Date', 
                                                'class': 'form-control',
                                                'cols': 30,
                                            }
                                        )
                                    ) 
    current_stock           = forms.IntegerField(min_value=0)  
    manufacturer            = forms.CharField(max_length = 30)
    price                   = forms.DecimalField(decimal_places = 2, max_digits = 8, min_value=0.01)
    featured_status         = forms.BooleanField(required=False) 
    featured_promo_overlay  = forms.ImageField(required=False) 



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