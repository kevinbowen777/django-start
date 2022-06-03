from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the Homepage")


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About page")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the About page")
