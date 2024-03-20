"""
Тесты для привычек
"""

import string

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, UserRoles
from habits.models import Habits


class HabitsTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Тестовый пользователь и тестовая привычка
        """
        self.user = User(email='test@test.ru',
                         phone='111111111',
                         city='Testograd',
                         is_superuser=False,
                         is_staff=False,
                         is_active=True,
                         role=UserRoles.MEMBER,
                         id_tg=123456789
                         )
        self.user.set_password('123QWE456RTY')
        self.user.save()
        
        response = self.client.post(
            '/users/token/',
            {"email": "test@test.ru", "password": "123QWE456RTY"}
        )
        
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}
        
        self.habit = Habits.objects.create(
            name="Привычка тест",
            owner=self.user,
            place="Место тренировки",
            time="7:30",
            action="Начать работать",
            is_pleasure=False,
            associated_habits=None,
            periodic=1,
            award="Съесть печеньку",
            time_exec="00:02",
            is_public=False
        )
    
    def test_create_habits(self):
        """
        Тест операции создания (create) привычки
        """
        data = {
            "name": "Привычка тест 1",
            "owner": self.user.id,
            "place": "Работа",
            "time": "8:30",
            "action": "Ходить",
            "is_pleasure": False,
            "associated_habits": None,
            "periodic": 1,
            "award": "Выпить чай",
            "time_exec": "00:02",
            "is_public": False
        }
        create_habit = reverse('habits:habits_create')
        response = self.client.post(create_habit, data,
                                    format="json", **self.headers)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], data['name'])
    
    def test_retrieve_habits(self):
        """
        Тест операции чтения (retrieve) привычки
        """
        retrieve_url = reverse('habits:habits_detail',
                               args=[self.habit.id])
        response = self.client.get(retrieve_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.habit.name)
    
    def test_update_habits(self):
        """
        Тест операции обновления (update) привычки
        """
        update_url = reverse('habits:habits_update',
                             args=[self.habit.id])
        updated_data = {
            "name": "обновляем привычку",
            "place": "Сигнал",
        }
        response = self.client.patch(update_url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.name, updated_data['name'])
        self.assertEqual(self.habit.place, updated_data['place'])
    
    def test_delete_habits(self):
        """
        Тест операции удаления (delete) привычки
        """
        delete_url = reverse('habits:habits_delete',
                             args=[self.habit.id])
        response = self.client.delete(delete_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habits.objects.filter(id=self.habit.id).exists())
    
    def test_list_habits(self):
        """
        Тест операции получения списка привычек
        """
        list_url = reverse('habits:habits_list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], self.habit.name)
    
    def test_str_habits(self):
        my_str: string = self.habit.__str__()
        self.assertEqual(my_str, "Привычка тест Начать работать")
