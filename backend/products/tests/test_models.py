from django.test import TestCase
from datetime import date
from products.models import Category, Discount, Product, ProductImage
from restaurants.models import Restaurant


class ModelTestCase(TestCase):
    def setUp(self):
        # Create a sample restaurant
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', rate=3.0,location='123 Main St',road='address',city='city')
        self.category = Category.objects.create(name="Test Category")

        # Create a sample discount
        self.discount = Discount.objects.create(
            code="TESTCODE", percentage=10.00,
            start_date=date.today(),
            end_date=date.today()
        )

        # Create a sample product
        self.product = Product.objects.create(
            name="Test Product", price=50.00,
            description="Test description",
            available_quantity=100,
            category=self.category,
            discount=self.discount,
            restaurant=self.restaurant
        )

        # Create a sample product image
        self.product_image = ProductImage.objects.create(
            product=self.product,
            image="path/to/test/image.jpg"
        )

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_discount_str_method(self):
        self.assertEqual(str(self.discount), "TESTCODE")

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_product_image_product_relation(self):
        self.assertEqual(self.product_image.product, self.product)

    def test_product_image_image_path(self):
        self.assertEqual(self.product_image.image, "path/to/test/image.jpg")

    def test_product_category_relation(self):
        self.assertEqual(self.product.category, self.category)

    def test_product_discount_relation(self):
        self.assertEqual(self.product.discount, self.discount)

    def test_product_restaurant_relation(self):
        self.assertEqual(self.product.restaurant, self.restaurant)
