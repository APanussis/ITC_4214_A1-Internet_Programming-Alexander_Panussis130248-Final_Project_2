from django.contrib import admin

from .models import ModelProduct, ModelCategory, ModelManufacturer

#QoL change: 
#   list_display:
#       Display the id and name field of ModelProduct entries instead of the 
#       default abstract entry counter in the admin webpage.
#   search_fields:
#       Create a simple searchbox so that superusers can directly search model entries by 'name' or by 'description'.

class ModelProductAdmin(admin.ModelAdmin):  
    list_display = ['id', 'name']
    search_fields = ['name', 'discription']

# Register your models here.

admin.site.register(ModelProduct, ModelProductAdmin)
admin.site.register(ModelCategory)
admin.site.register(ModelManufacturer)