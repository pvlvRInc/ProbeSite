from django.contrib import admin
from news.models import News,Category
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','is_published')
    list_filter = ('category','is_published')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)