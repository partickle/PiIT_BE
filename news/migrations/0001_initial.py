# Generated by Django 5.0.5 on 2024-06-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='news_photos/', verbose_name='Фото')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата выкладки')),
            ],
        ),
    ]
