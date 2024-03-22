from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.
def about_page(request):
  """ 
  View to render the About page
  """
  about = About.objects.all()

  return render(
    request,
    "about/about.html",
    {
      "about": about
    }
  )