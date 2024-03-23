"""
Сериализатор для модели Привычка
"""

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import Habits
from habits.validators import exclude_validator
from users.models import User


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = ['name',
                  'owner',
                  'place',
                  'time',
                  'action',
                  'is_pleasure',
                  'associated_habits',
                  'periodic',
                  'award',
                  'time_exec',
                  'is_public'
                  ]
        validators = [exclude_validator,]


class HabitsListSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Habits
        fields = ['name',
                  'owner',
                  'place',
                  'time',
                  'action',
                  'is_pleasure',
                  'associated_habits',
                  'periodic',
                  'award',
                  'time_exec',
                  'is_public'
                  ]
