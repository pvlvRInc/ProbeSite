from django.urls import path
from news.views import NewsListView, CategoryNewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('<int:category_id>', CategoryNewsListView.as_view(), name='category_news')
]
