from django import forms
from django.shortcuts import redirect

from recipes.models import Rating

from recipes.models import Recipe


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
