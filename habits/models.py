"""
Модель привычки для сервера полезных привычек.
"""

from django.db import models

from users.models import NULLABLE


class Habits(models.Model):
    """
    - name - Наименование привычки.
    - owner - Пользователь — создатель привычки.
    - place - Место где необходимо выполнять привычку.
    - time - Время, когда необходимо выполнять привычку.
    - action - Действие, которое представляет собой привычка.
    - is_pleasure - Признак приятной привычки — привычка, которую можно
    привязать к выполнению полезной привычки.
    - associated_habits - Связанная привычка — привычка, которая связана с
    другой привычкой, важно указывать для полезных привычек, но не
    для приятных.
    - periodic - Периодичность (по умолчанию ежедневная) — периодичность
    выполнения привычки для напоминания в днях.
    - award - Вознаграждение — чем пользователь должен себя вознаградить после
    выполнения привычки.
    - time_exec - Время на выполнение — время, которое предположительно
    потратит пользователь на выполнение привычки.
    - is_public - Признак публичности — привычки можно публиковать в общий
    доступ, чтобы другие пользователи могли брать в пример чужие привычки.
    """

    name = models.CharField(max_length=150, verbose_name='название')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE,
                              verbose_name='создатель', **NULLABLE,
                              related_name='owner')
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasure = models.BooleanField(default=True,
                                      verbose_name='признак приятной привычки')
    associated_habits = models.ForeignKey('self', on_delete=models.SET_NULL,
                                          **NULLABLE,
                                          verbose_name='связанная привычка',
                                          related_name='habits_associated')
    periodic = models.IntegerField(default=1,
                                   verbose_name='периодичность в днях')
    award = models.CharField(max_length=150, verbose_name='вознаграждение',
                             **NULLABLE)
    time_exec = models.TimeField(verbose_name='время на выполнение',
                                 **NULLABLE)
    is_public = models.BooleanField(default=True,
                                    verbose_name='признак публичности')

    def __str__(self):
        return f'{self.name} {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
