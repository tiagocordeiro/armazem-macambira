from django.test import TestCase, RequestFactory, Client

from .views import product_list


class ProductsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_status_code_is_200(self):
        request = self.factory.get('/produtos/')

        response = product_list(request)
        self.assertEqual(response.status_code, 200)
