from django.db.models import Count

from news.models import Category


class CategoriesMixin:

    def get_categories(self):
        return Category.objects.all().annotate(newscount=Count('news'))
