from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsView.as_view()),
    path('<str:slug>', views.full_new, name='full_new'),
]
