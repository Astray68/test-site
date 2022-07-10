from django.shortcuts import render
from django.views.generic.base import View
from .models import Review
from .forms import ReviewForm
from django.contrib import auth
from django.utils import timezone
from django.http import HttpResponse


class ReviewsView(View):
    reviews = Review.objects.filter(status=3).order_by('-date_posted')
    """List reviews"""
    def get(self, request):
        if request.user.is_authenticated:
            form = ReviewForm()
        else:
            form = None
        return render(request, 'reviews/review.html', {'review_list': self.reviews, 'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        name = auth.get_user(request)
        date_posted = timezone.now()
        rez = form.save(commit=False)
        rez.name = name
        rez.date_posted = date_posted
        rez.save()
        return HttpResponse('Your review has been successfully submitted for moderation <a href="/">Home</a>')
