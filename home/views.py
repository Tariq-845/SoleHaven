from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    """
    Template view to display the home page
    (index.html)
    """
    template_name = 'home/index.html'
    