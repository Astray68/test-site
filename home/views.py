from django.shortcuts import render
from django.views.generic.base import View
from services.models import Product
from news.models import New
from .models import Banner


class HomeView(View):
    """
    List 3 news, 2 banners, 3 services
    """
    def get(self, request):
        news = New.objects.filter(is_deleted=False, show_in_home=True).order_by('-date_posted')[:3]
        products = Product.objects.filter(is_deleted=False, show_in_home=True).order_by('-id')[:3]
        banners = Banner.objects.filter(is_deleted=False, show_in_home=True).order_by('-id')[:3]
        return render(request, 'home/home.html', {'3_latest_news': news, '3_last_products': products,
                                                  'banners': banners})
