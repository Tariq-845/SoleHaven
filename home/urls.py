from djang.urls import path
from . import views

urlpatterns = [
  path('', Index.as_view(), name='home')
]