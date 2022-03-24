from django.contrib import admin
from news.models import News,Category
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','is_published', 'photo')
    list_filter = ('category','is_published')
    search_fields = ('title','created_at')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('title',)

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)