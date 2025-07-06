from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):

    def test_create_user(self):
        email = 'ghdfkgml@naver.com'
        password = 'ghdfkgml123'

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        email = 'ghdfkgml_super@naver.com'
        password = 'ghdfkgml123'

        super_user = get_user_model().objects.create_superuser(
            email=email, password=password
        )

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)