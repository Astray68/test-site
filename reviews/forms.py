from django import forms
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Write there your review'
                }
            )
        }

    def clean_review(self):
        review = self.cleaned_data['message']
        return review
