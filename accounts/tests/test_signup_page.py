from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from ..views import SignupPageView


class SignupPageTests(TestCase):
    def setUp(self):
        self.username = "newuser"
        self.email = "newuser@example.com"
        url = reverse("account_signup")
        self.response = self.client.get(url)

        User = get_user_model()
        self.new_user = User.objects.create_user(
            username=self.username,
            email=self.email,
        )

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(
            self.response, "Hi there! I should not be on the page."
        )

    def test_signup_form(self):
        User = get_user_model()
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertEqual(User.objects.all()[0].email, self.email)

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__,
        )
