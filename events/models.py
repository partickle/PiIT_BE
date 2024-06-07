from django.db import models
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    event_date = models.DateTimeField(verbose_name="Дата проведения")

    def __str__(self):
        return self.title
