from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','image','rating','description','price']
admin.site.register(Product,ProductAdmin)