from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

class UserAuthenticationTest(TestCase):

    def test_login_success_with_correct_details(self):

        def setUp(self):
            User = get_user_model()
            user = User.objects.creat_user('temporary', 'abc@company.com', 'temporary')

        def test_login_success(self):
            User = get_user_model()
            self.client.login(username='temporary', password='temporary')
            response = self.client.get('/home/', follow=True)
            user = User.objects.get(username='temporary')
            self.assertEqual(response.context['email'], 'abc@company.com')

    def test_login_fail_with_incorrect_details(self):

        def setUp(self):
            User = get_user_model()
            user = User.objects.creat_user('temporary', 'abc@company.com', 'temporary')
        def test_login_fail(self):
            User = get_user_model()
            self.client.login(username='temporary', password='tempor')
            response = self.client.get('/login/', follow=True)
            user = User.objects.get(username='temporary')
            self.assertEqual(response.context['email'], '')

    def test_user_register_fail(self):

            User = get_user_model()
            user = User.objects.creat_user('temporary', 'abc@company.com', '')
            response = self.client.get('/register/', follow=True)
