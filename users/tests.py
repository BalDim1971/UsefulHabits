"""
Тесты для пользователя
"""
import string

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, UserRoles


class UsersTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Тестовый пользователь
        """
        self.user = User(email='admin@sky.pro',
                         phone='111111111',
                         city='admin',
                         is_superuser=True,
                         is_staff=True,
                         is_active=True,
                         role=UserRoles.MODERATOR,
                         id_tg=123456789
                         )
        self.user.set_password('123QWE456RTY')
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {"email": "admin@sky.pro", "password": "123QWE456RTY"}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}

    def test_create_user(self):
        """
        Тест операции создания (create) пользователя
        """
        data = {
            "email": "test1@test.ru",
            "phone": "123456789",
            "city": "Testity1",
            "is_superuser": False,
            "is_staff": False,
            "is_active": True,
            "role": UserRoles.MEMBER,
            "id_tg": 987654321,
            "password": "123456789",
        }
        create_user = reverse('users:user_create')
        response = self.client.post(create_user, data,
                                    format="json", **self.headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], data['email'])

    def test_retrieve_user(self):
        """
        Тест операции чтения (retrieve) пользователя
        """
        retrieve_url = reverse('users:user_detail',
                               args=[self.user.id])
        response = self.client.get(retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    # def test_update_user(self):
    #     """
    #     Тест операции обновления (update) пользователя
    #     """
    #     update_url = reverse('users:user_update',
    #                          args=[self.user.id])
    #     print(update_url)
    #     updated_data = {
    #         "city": "Mycity",
    #         "phone": "222222222",
    #     }
    #     response = self.client.patch(update_url, updated_data, format='json')
    #     print(response.json())
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.user.refresh_from_db()
    #     self.assertEqual(self.user.phone, updated_data['phone'])
    #     self.assertEqual(self.user.city, updated_data['city'])
    #
    # def test_delete_user(self):
    #     """
    #     Тест операции удаления (delete) пользователя
    #     """
    #     delete_url = reverse('users:user_delete',
    #                          args=[self.user.id])
    #     response = self.client.delete(delete_url)
    #
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(User.objects.filter(id=self.user.id).exists())
    #
    def test_list_user(self):
        """
        Тест операции получения списка пользователя
        """
        list_url = reverse('users:user_list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)

    def test_str_user(self):
        """
        Тест проверки получения строки...
        """
        my_str = str(self.user)
        self.assertEqual(my_str, "admin@sky.pro")
