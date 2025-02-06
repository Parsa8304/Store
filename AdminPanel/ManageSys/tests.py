from django.test import TestCase
from .models import Product
from decimal import Decimal
from django.urls import reverse



#Product model testing to see if it is created correctly or not!
class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", price=Decimal('9.99'))

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.price, Decimal('9.99'))

    def test_product_string_representation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(str(product), "Test Product")

#____________________________________________________


#Views testing to make sure our funcs render correctly
class ProductViewTest(TestCase):

    def setUp(self):
        Product.objects.create(name="Test Product", price=Decimal('9.99'))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ManageSys/products.html')
