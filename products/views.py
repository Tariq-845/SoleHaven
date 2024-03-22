from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Product, Review
from .forms import ReviewForm

# Create your views here.


def product_page(request):
    """ 
    View to render the product page
    """
    products = Product.objects.all().order_by('name')
  
    return render(
      request,
      'products/products.html',
      {
          'products': products
      }
    )


def product_detail(request, pk):
    """
    View to render the product detail pages and
    allow valid users to post reviews 
    """
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


def review_edit(request, pk, review_id):
    """
    View for users to edit their reviews
    """
    if request.method == "POST":
      product = get_object_or_404(Product, pk=pk)
      review = get_object_or_404(Review, pk=review_id)
      review_form = ReviewForm(data=request.POST, instance=review)

      if review_form.is_valid() and review.author == request.user:
        review = review_form.save(commit=False)
        review.product = product
        review.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your review has been updated successfully!'
        )
      else:
          messages.add_message(
              request,
              messages.ERROR,
              'There was an error trying to update your review'
          )
    
    return HttpResponseRedirect(reverse('product_detail', args=[pk]))


def review_delete(request, pk, review_id):
    """
    View for users to delete their reviews
    """
    product = get_object_or_404(Product, pk=pk)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your review has been successfully deleted!'
      )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'There was an error trying to delete your review'
        )
  
    return HttpResponseRedirect(reverse('product_detail', args=[pk]))
