# Generated by Django 5.0.1 on 2024-03-22 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['email', 'first_name', 'last_name'], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
