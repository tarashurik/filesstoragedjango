import os

from django.contrib.auth.models import User
from django.test import TestCase
from filesstoragedjango.settings import BASE_DIR


simple_file_dir = os.path.join(BASE_DIR, 'files_to_test/simple_file.txt')
copy_file_dir = os.path.join(BASE_DIR, 'files_to_test/simple_file_copy.txt')
too_big_file_dir = os.path.join(BASE_DIR, 'files_to_test/large_file.txt')

file_url = '/api/files/'
register_url = '/api/users/register/'

user_data = {
    'username': 'admin',
    'password': 'admin',
}


class FilesTest(TestCase):
    def register_admin(self):
        self.client.post(register_url, data=user_data)
        user = User.objects.all()[0]
        return user

    def test_simple_file_upload(self):
        self.register_admin()
        self.client.login(username=user_data.get('username'), password=user_data.get('password'))

        with open(simple_file_dir, 'rb') as file:
            data = {'file': file}
            response = self.client.post(file_url, data=data)
        self.assertEqual(response.status_code, 201)

    def test_simple_file_copy_upload(self):
        self.register_admin()
        self.client.login(username=user_data.get('username'), password=user_data.get('password'))

        with open(simple_file_dir, 'rb') as file:
            data = {'file': file}
            self.client.post(file_url, data=data)

        with open(copy_file_dir, 'rb') as file_copy:
            data = {'file': file_copy}
            response = self.client.post(file_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('You have already have File with same content' in str(response.content))

    def test_too_big_file_upload(self):
        self.register_admin()
        self.client.login(username=user_data.get('username'), password=user_data.get('password'))

        with open(too_big_file_dir, 'rb') as file_too_big:
            data = {'file': file_too_big}
            response = self.client.post(file_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('Your file too big' in str(response.content))

