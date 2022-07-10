from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import New


class NewsView(View):
    """
    List news
    """
    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            news = New.objects.filter(is_deleted=False,
                                      date_posted__range=[start_date, end_date]).order_by('-date_posted')
        else:
            news = New.objects.filter(is_deleted=False).order_by('-date_posted')
        return render(request, 'news/news.html', {'news_list': news})


def full_new(request, slug):
    """
    Full news page
    """
    new_content = get_object_or_404(New, slug=slug, is_deleted=False)
    return render(request, 'news/full_new.html', {'content': new_content})
