from PIL import Image
import datetime
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import ModelUser

class FormProfileCreate(forms.ModelForm):
    name                    = forms.CharField(max_length = 60)
    email                   = forms.EmailField()
    image                   = forms.ImageField(required=False) 
    description             = forms.CharField(widget=forms.Textarea, required=False)    #TextArea widget to give the user space 
                                                                                        #to write something more than a single sentence.
    
    # date_joined               = forms.DateField(                          # SHOULD BE AUTOMATED 
    #                                 initial=datetime.date.today,
    #                                 widget= forms.DateInput 
    #                                     (attrs=
    #                                         {                       
    #                                             'type':'date',
    #                                             'class': 'form-control',
    #                                             'cols': 30,
    #                                         }
    #                                     )
    #                                 )

    age                     = forms.IntegerField(min_value=0, required=False)  
    #orders_made             = forms.IntegerField(min_value=0, default=0)    # SHOULD BE AUTOMATED 

    #REFERENCE MODEL
    # name = models.CharField(max_length = 60, unique = True)
    # email = models.EmailField(blank=False, null = False, unique = True)
    # image = models.ImageField(blank=True, null=True, upload_to="userImages/")
    # description = models.TextField(blank = True, null = True)
    # date_joined = models.DateField(blank=False, null = False)
    # age = models.PositiveIntegerField(blank = True, null = True, default=0)
    # orders_made = models.PositiveIntegerField(default=0)

    class Meta:
        model = ModelUser
        fields = [
            'name',
            'email',
            'image',
            'description',
            #'date_joined',
            'age',
            #'orders_made',
        ]