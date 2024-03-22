from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

SIZE_CHOICES = (
  ('SIZE 6', 'Size 6'),
  ('SIZE 7', 'Size 7'),
  ('SIZE 8', 'Size 8'),
  ('SIZE 9', 'Size 9'),
  ('SIZE 10', 'Size 10'),
  ('SIZE 11', 'Size 11'),
  ('SIZE 12', 'Size 12'),
)


class Product(models.Model):
  
    """
    Model to create products items
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = CloudinaryField('image', default='placeholder')
    sizes = forms.ChoiceField(
      choices = SIZE_CHOICES,
      widget=forms.Select(),
    )

    def __str__(self):
      return self.name


class Review(models.Model):
    """
    Model to display reviews on product details
    """
    product = models.ForeignKey(
      Product,
      on_delete=models.CASCADE,
      related_name='reviews'
    )
    author = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name='review_author'
    )
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
      """ 
      Ordering by date
      """
      ordering = ['date_posted']

    def __str__(self):
      return f'Review {self.body} by {self.author}'
