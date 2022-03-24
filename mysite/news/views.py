from django.shortcuts import render
from django.views.generic import ListView
from news.models import News
from news.utils import CategoriesMixin


def main_path(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})


class NewsListView(CategoriesMixin, ListView):
    model = News
    queryset = News.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, 'news/news_list.html', {'news': self.queryset, 'categories': super().get_categories()})


class CategoryNewsListView(NewsListView):

    def get(self, request, *args, **kwargs):
        category_id = kwargs.pop('category_id')

        context = {
            'news': self.queryset.filter(category__id=category_id),
            'categories': super().get_categories(),
            'category_id': category_id
        }

        return render(request, 'news/news_list.html', context)
