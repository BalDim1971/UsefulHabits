"""
Модель пользователя для сервера привычек.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """
    Класс, описывающий модель пользователь
    Авторизация меняется на email
    Стандартная модель расширяется:
    «Номер телефона»,
    «Аватар»,
    «Страна».
    """

    username = None
    email = models.EmailField(max_length=200, verbose_name='электронная почта',
                              unique=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',
                               **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices,
                            default=UserRoles.MEMBER, verbose_name='роль',
                            **NULLABLE)
    is_active = models.BooleanField(default=True,  verbose_name='активность')
    id_tg = models.CharField(max_length=15,
                             verbose_name='ID бота TG', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['email', 'first_name', 'last_name']
