from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class TeacherManager(BaseUserManager):
    def create_user(self, usertag, password=None, **extra_fields):
        if not usertag:
            raise ValueError('The UserTag field must be set')
        user = self.model(usertag=usertag, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usertag, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(usertag, password, **extra_fields)


class Teacher(AbstractBaseUser, PermissionsMixin):
    usertag = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = TeacherManager()

    USERNAME_FIELD = 'usertag'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.usertag
