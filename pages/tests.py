from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class AboutPageTests(SimpleTestCase):
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_url_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
