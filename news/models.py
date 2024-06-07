from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    photo = models.ImageField(upload_to='news_photos/', verbose_name="Фото")
    content = models.TextField(verbose_name="Содержание")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата выкладки")

    def __str__(self):
        return self.title
