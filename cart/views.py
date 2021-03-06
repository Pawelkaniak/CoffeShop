from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product
from .forms import CartAddProductForm


@require_POST
def cart_add(request,product_id):
    cart=Cart(request)
    form = CartAddProductForm(require_POST)
    product = get_object_or_404(Product,id=product_id)
    if form.is_valid():
        cd= form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],quantity_updated=cd['update'])
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart=Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})

def cart_remove(request,product_id):
    cart=Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')






# Create your views here.
