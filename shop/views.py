from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Product
# Create your views here.

def index(request,category_slug):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filters(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html' ,{'category':category, 'categories':categories, 'products':products})

def product_detail(request,product_id,product_slug):
    product = get_object_or_404(Product,id=product_id, slug=product_slug, available=True) #slug is for SEO
    return render(request, 'shop/product/detail.html', {'product':product})



    #return render(request,'/shop/base.html',{})
