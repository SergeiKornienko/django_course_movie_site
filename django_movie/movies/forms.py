from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Form of review."""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
