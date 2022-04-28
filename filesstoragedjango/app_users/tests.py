from django.test import TestCase
from django.contrib.auth.models import User


user_data = {
    'username': 'admin',
    'password': 'admin',
}

register_url = '/api/users/register/'


class UsersTest(TestCase):
    def test_register_new_user(self):
        user = User.objects.all()
        self.assertFalse(user)

        response = self.client.post(register_url, data=user_data)
        self.assertEqual(response.status_code, 201)

        user = User.objects.all()[0]
        self.assertEqual(user.username, user_data['username'])
