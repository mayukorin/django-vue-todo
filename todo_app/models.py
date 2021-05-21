from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.utils import timezone
from django.conf import settings
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('メールアドレスは必須です')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        user = self.create_user(
            email,
            password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

    def create_staff(self, email, password, **extra_fields):

        user = self.create_user(
            email,
            password,
            **extra_fields,
        )
        user.is_superuser = False
        user.is_staff = True

        user.save(using=self._db)
        return user

class User(AbstractUser):

    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(verbose_name='ユーザ名', max_length=150, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]


class Task(models.Model):

    class Meta:
        db_table = 'task'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    content = models.TextField(verbose_name='内容', blank=True)
    deadline = models.DateField(verbose_name='締切日', default=timezone.now, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)


    