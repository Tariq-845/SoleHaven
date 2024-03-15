from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ReviewForm

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

  if request.method == "POST":
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
      review = review_form.save(commit=False)
      review.author = request.user 
      review.products = products
      review.save()

  review_form = ReviewForm()

  return render(
    request,
    'products/products_detail.html',
    {
      'products': products,
      'reviews': reviews,
      'review_count': review_count,
      'review_form': review_form
    }
  )