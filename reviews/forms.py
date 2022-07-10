from django.forms import ModelForm, Textarea
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
