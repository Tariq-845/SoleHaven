from django.shortcuts import render, get_object_or_404
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

def product_detail(request, pk):
  products = get_object_or_404(Product, pk=pk)
  reviews = products.reviews.all()
  review_count = products.reviews.all().count()

  return render(
    request,
    'products/products_detail.html',
    {
      'products': products,
      'reviews': reviews,
      'review_count': review_count,
    }
  )