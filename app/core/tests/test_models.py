from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """ Test creating a new user with an email is successful """

        email = 'test@london.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@LONDON.com'
        user = get_user_model().objects.create_user(email, '123123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123123')

    def test_create_new_superuser(self):
        """ Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            email='test@london.com',
            password='testpass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
