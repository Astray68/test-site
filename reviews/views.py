from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


class ReviewsView(View):
    model = Review

    form_class = ReviewForm




    """List reviews"""
    def get(self, request):
        reviews = Review.objects.filter(status=3).order_by('-date_posted')
        return render(request, 'reviews/review.html', {'review_list': reviews})


@login_required
@require_http_methods(["POST"])
def post_review(request):
    form_review = ReviewForm(request.POST)
    review_inst = Review.objects.all()
    if request.method == 'POST':
        if form_review.is_valid():
            form_review.save()
            return redirect('reviews')
        return render(request, 'reviews/review.html', {'form_review': form_review})
