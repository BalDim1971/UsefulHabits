# Generated by Django 5.0.1 on 2024-03-13 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('place', models.CharField(max_length=150, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=150, verbose_name='действие')),
                ('is_pleasure', models.BooleanField(default=True, verbose_name='признак приятной привычки')),
                ('periodic', models.IntegerField(default=1, verbose_name='периодичность в днях')),
                ('award', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('time_exec', models.TimeField(blank=True, null=True, verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='признак публичности')),
                ('associated_habits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habits_associated', to='habits.habits', verbose_name='связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
