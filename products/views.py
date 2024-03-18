from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Review
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
  product = get_object_or_404(Product, pk=pk)
  reviews = product.reviews.all()
  review_count = product.reviews.all().count()
  review_form = ReviewForm()

  if request.method == "POST":
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
      review = review_form.save(commit=False)
      review.author = request.user 
      review.product = product
      review.save()
      messages.add_message(
        request,
        messages.SUCCESS,
        'Your review has successfully been posted'
      )

  return render(
    request,
    'products/products_detail.html',
    {
      'product': product,
      'reviews': reviews,
      'review_count': review_count,
      'review_form': review_form
    }
  )