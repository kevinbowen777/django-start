from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Homepage")

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "Not the Homepage")


class AboutPageTests(SimpleTestCase):
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_url_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")
