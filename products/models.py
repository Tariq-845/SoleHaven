from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

SIZE_CHOICES = (
  (0, 'Size 6'),
  (1, 'Size 7'),
  (2, 'Size 8'),
  (3, 'Size 9'),
  (4, 'Size 10'),
  (5, 'Size 11'),
  (6, 'Size 12'),
)

class Product(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  product_image = CloudinaryField('image', default='placeholder')
  sizes = models.IntegerField(
    choices = SIZE_CHOICES,
    default=0
  )

  def __str__(self):
    return self.name

class Review(models.Model):
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
    ordering = ['date_posted']

  def __str__(self):
    return f'Review {self.body} by {self.author}'