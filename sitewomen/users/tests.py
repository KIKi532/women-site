from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .forms import RegisterUserForm
from django.contrib.auth.models import User

class UserRegistrationViewCase(TestCase):
    """Тести для авторизіції/рейстрації"""

    def setUp(self):
        self.path = reverse('users:register')

    def test_user_registration_get(self):
        response = self.client.get(self.path)


        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Реєстрація')
        self.assertTemplateUsed(response, 'users/register.html')

