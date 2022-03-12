from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#todo crate path with all existing news
#todo make a template

def main_path(request):
    return HttpResponse('Hello, world!')