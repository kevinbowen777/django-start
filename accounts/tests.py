from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .views import SignupPageView


class CustomUserTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )

        self.super_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@example.com",
            password="T3stP@5s123",
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, "kevin")
        self.assertEqual(self.user.email, "kevin@example.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_user_asserts(self):
        User = get_user_model()
        try:
            self.assertIsNotNone(self.user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="", password="foo")

    def test_create_superuser(self):
        self.assertEqual(self.super_user.username, "superadmin")
        self.assertEqual(self.super_user.email, "superadmin@example.com")
        self.assertTrue(self.super_user.is_active)
        self.assertTrue(self.super_user.is_staff)
        self.assertTrue(self.super_user.is_superuser)

    def test_superuser_asserts(self):
        User = get_user_model()
        try:
            self.assertIsNotNone(self.super_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="",
                email="super@user.com",
                password="foo",
                is_superuser=False,
            )

    def test___str__(self):
        assert self.user.__str__() == self.user.username
        assert str(self.user) == self.user.username


class SignupPageTests(TestCase):

    username = "newuser"
    email = "newuser@example.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(
            self.response, "Hi there! I should not be on the page."
        )

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(  # noqa: F841
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].username, self.username
        )
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__,
        )
