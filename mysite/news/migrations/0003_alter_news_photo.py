# Generated by Django 4.0.3 on 2022-03-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_options_alter_news_options_news_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
