from django.test import TestCase, RequestFactory, Client

from .views import index


class WebsiteHomeTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_status_code_is_200(self):
        request = self.factory.get('/')

        response = index(request)
        self.assertEqual(response.status_code, 200)
