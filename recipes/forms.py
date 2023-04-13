from django import forms


from recipes.models import Rating
from recipes.models import Recipe


from django.shortcuts import redirect


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name",
            "author",
            "description",
            "image",
        ]

from recipes.models import Recipe


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
