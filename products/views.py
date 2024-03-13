from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def product_page(request):
  products = Product.objects.all().order_by('name')
  
  return render(
    request,
    'products/products.html',
    {
      'products': products
    }
  )