"""
Тесты для пользователя
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User, UserRoles


class UsersTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Тестовый пользователь
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
        }
        create_user = reverse('users:user_create')
        response = self.client.post(create_user, data,
                                    format="json", **self.headers)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], data['email'])
