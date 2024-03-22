from . import views
from django.urls import path

urlpatterns = [
  path('', views.product_page, name='browse'),
  path('<int:pk>/', views.product_detail, name='product_detail'),
  path(
    '<int:pk>/edit_review/<int:review_id>',
    views.review_edit, name='review_edit'),
  path(
    '<int:pk>/delete_review/<int:review_id>',
    views.review_delete, name='review_delete'),
]
