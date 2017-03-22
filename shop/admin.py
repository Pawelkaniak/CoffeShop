from django.contrib import admin
from .models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
    

class CategoryADms



# Register your models here.
