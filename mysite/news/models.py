from django.db import models
from django.shortcuts import render
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    # todo add image field

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return 'Новость'


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('category_news', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

# Create your models here.
