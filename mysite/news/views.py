from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#todo crate path with all existing news
#todo make a template

def main_path(request):
    print(request)
    return render(request, 'news/main_path.html',{})