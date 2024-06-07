# news/urls.py
from django.urls import path
from .views import NewsListCreateView, NewsDetailView

urlpatterns = [
    path('', NewsListCreateView.as_view(), name='news_list_create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
