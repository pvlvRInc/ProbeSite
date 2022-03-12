from django.urls import path
from news.views import main_path

urlpatterns = [
    path('',main_path)
]