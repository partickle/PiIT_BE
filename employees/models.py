from django.db import models


class Employee(models.Model):
    photo = models.ImageField(upload_to='photos/')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    total_experience = models.PositiveIntegerField()
    specialized_experience = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name} - {self.position}"
