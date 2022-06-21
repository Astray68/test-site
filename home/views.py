from django.shortcuts import render
from django.views.generic.base import View

from news.models import New

class HomeView(View):
    """List news"""
    def get(self, request):
        news = New.objects.filter(is_deleted=False).order_by('-date_posted')[:3]
        return render(request, 'home/home.html', {'3_latest_news': news})

