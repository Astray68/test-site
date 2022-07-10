from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesView.as_view()),
    path('category/<str:slug>/', views.category_view, name='category_view'),
]
