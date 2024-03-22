from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Review form model to create reviews
    """

    class Meta:
        model = Review
        fields = ("body",)
