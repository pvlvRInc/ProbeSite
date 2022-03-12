from django.http import HttpResponse
from django.shortcuts import render
from news.models import News
# Create your views here.
#todo crate path with all existing news
#todo make a template

def main_path(request):
    print(request)
    news = News.objects.all()
    return render(request, 'news/main_path.html',{'news': news})