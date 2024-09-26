# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from restaurants.models import Restaurant
# from products.models import Category, Discount, Product, ProductImage
# from products.serializers import CategorySerializer, DiscountSerializer, ProductImageSerializer, ProductSerializer
# from datetime import date


# class SerializerTestCase(TestCase):
#     def setUp(self):
#         # Create a sample category
#         self.category = Category.objects.create(name="Test Category")
#         self.restaurant = Restaurant.objects.create(name='Test Restaurant', rate=3.0,location='123 Main St',road='address',city='city')

#         # Create a sample discount
#         self.discount = Discount.objects.create(
#             code="TESTCODE",
#             percentage=10.00,
#             start_date=date.today(),
#             end_date=date.today()
#         )

#         # Create a sample product
#         self.product = Product.objects.create(
#             name="Test Product",
#             price=50.00,
#             description="Test description",
#             available_quantity=100,
#             category=self.category,
#             discount=self.discount,
#         )

#         # Create a sample product image
#         image_data = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
#         self.product_image = ProductImage.objects.create(product=self.product, image=image_data)

#     def test_category_serializer(self):
#         serializer = CategorySerializer(instance=self.category)
#         expected_data = {
#             'id': str(self.category.id),
#             'name': 'Test Category',
#         }
#         self.assertEqual(serializer.data, expected_data)

#     def test_discount_serializer(self):
#         serializer = DiscountSerializer(instance=self.discount)
#         expected_data = {
#             'id': str(self.discount.id),
#             'code': 'TESTCODE',
#             'percentage': '10.00',
#             'start_date': str(date.today()),
#             'end_date': str(date.today()),
#         }
#         self.assertEqual(serializer.data, expected_data)

#     def test_product_image_serializer(self):
#         serializer = ProductImageSerializer(instance=self.product_image)
#         expected_data = {
#             'id': str(self.product_image.id),
#             'product': str(self.product.id),
#             'image': self.product_image.image.url,
#         }
#         self.assertEqual(serializer.data, expected_data)

#     def test_product_serializer(self):
#         serializer = ProductSerializer(instance=self.product)
#         expected_data = {
#             'id': str(self.product.id),
#             'available_quantity': 100,
#             'name': 'Test Product',
#             'description': 'Test description',
#             'price': '50.00',
#             'category': str(self.category.id),
#             'discount': str(self.discount.id),
#             'restaurant':  str(self.restaurant.id) ,
#             'images': [
#                 {
#                     'id': str(self.product_image.id),
#                     'product': str(self.product.id),
#                     'image': self.product_image.image.url,
#                 }
#             ],
#         }
#         self.assertEqual(serializer.data, expected_data)
