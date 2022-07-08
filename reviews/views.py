from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Review
from .forms import ReviewForm
from django.contrib import auth
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


class ReviewsView(View):
    reviews = Review.objects.filter(status=3).order_by('-date_posted')
    """List reviews"""
    def get(self, request):
        if request.user.is_authenticated:
            form = ReviewForm()
        else:
            form = None
        return render(request, 'reviews/review.html', {'review_list': self.reviews, 'form': form})

    @login_required
    @require_http_methods(["POST"])
    def post(self, request):
        form = ReviewForm(request.POST)
        name = auth.get_user(request)
        date_posted = timezone.now()
        rez = form.save(commit=False)
        rez.name = name
        rez.date_posted = date_posted
        rez.save()
        return HttpResponse('Your review has been successfully submitted for moderation')


"""
@login_required
@require_http_methods(["POST"])
def post_review(request):
    form_review = ReviewForm(request.POST)
    review_inst = Review.objects.all()
    if request.method == 'POST':
        if form_review.is_valid():
            form_review.save()
            return redirect('reviews')
        return render(request, 'reviews/review.html', {'form': form_review})
"""

