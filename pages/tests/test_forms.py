from django.core.mail import BadHeaderError
from django.test import SimpleTestCase
from django.urls import reverse


class ContactFormTests(SimpleTestCase):
    def setUp(self):
        url = reverse("contact")
        self.response = self.client.get(url)
        self.form_data = {
            "from_email": "joe@example.com",
            "subject": "Test Email",
            "message": "This is a test email",
        }

    def test_contact_page_form_is_valid(self):
        response = self.client.post(
            "/contact/",
            data={
                "from_email": "joe@example.com",
                "subject": "Test Email",
                "message": "This is a test email",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_header_injection(self):
        error_occured = True
        try:
            self.client.post(
                "/contact/",
                data={
                    "from_email": "joe@example.com",
                    "subject": "Subject\nInjectionTest",
                    "message": "This is a test of a BadHeaderError",
                },
            )
            error_occured = False
        except BadHeaderError:
            error_occured = True
        self.assertFalse(error_occured)
