import pathlib
import uuid

from django.db import models
from decimal import Decimal 
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

def user_image_upload_handler(instance, filename): #upload files to seperate DIR so that same-name files dont overlap/overwrite eachother
    fpath = pathlib.Path(filename)
    newFileName = str(uuid.uuid1()) #uuid1 is uuid with time/datetime
    return f"userImages/{newFileName}{fpath.suffix}" #{fpath.suffix} includes file-name ending suffixes like .png and .jpg

class ModelProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(blank=True, null=True, upload_to=user_image_upload_handler)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

#Signals for extending User model by using the new fields of ModleProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ModelProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.modelprofile.save()