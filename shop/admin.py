from django.contrib import admin
from .models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available','created','updated']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)



# Register your models here.
