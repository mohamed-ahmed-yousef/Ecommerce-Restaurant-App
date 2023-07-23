from decimal import Decimal
import json
import os
import uuid

# from django.utils import timezone
categories_data = [
    {
        "model": "products.category",
        "pk": 1,
        "fields": {
            "name": "Category 1"  # Replace with the category name
        }
    },
    # Add more categories as needed...
]

# Generate data for Discount
discounts_data = [
    {
        "model": "products.discount",
        "pk": 1,
        "fields": {
            "code": "DISCOUNT25",  # Replace with the discount code
            "percentage": 22.5,  # Replace with the discount percentage
            "start_date":'2023-07-01',
            "end_date": '2023-07-15',
        }
    },
    # Add more discounts as needed...
]

# Generate data for Product
products_data = [
    {
        "model": "products.product",
        "pk": 1,
        "fields": {
            "name": "Product 1",  # Replace with the product name
            "price": 10.00,  # Replace with the product price
            "description": "Product 1 description.",  # Replace with the product description
            "available_quantity": 100,  # Replace with the available quantity of the product
            "created_at": '2023-07-01',
            "updated_at": '2023-07-15',
            "category": 1,  # Corresponds to the ID of the first category in categories_data
            "discount": 1,  # Corresponds to the ID of the first discount in discounts_data
            "restaurant": 1  # Replace with the ID of the Restaurant associated with the product
        }
    },
    # Add more products as needed...
]

# Generate data for ProductImage
product_images_data = [
    {
        "model": "products.productimage",
        "pk": 1,
        "fields": {
            "product": 1,  # Corresponds to the ID of the first product in products_data
            "image": "path/to/product1_image.jpg"  # Replace with the actual image path for Product 1
        }
    },
    # Add more product images as needed...
]

# Combine the generated data for all models
fixture_data = categories_data + discounts_data + products_data + product_images_data


current_directory = os.path.dirname(os.path.abspath(__file__))

# Set the filename for the fixture data JSON file
json_filename = "initial_data.json"

# Create the JSON file in the current directory
json_file_path = os.path.join(current_directory, json_filename)

with open(json_file_path, 'w') as outfile:
    json.dump(fixture_data, outfile)

import subprocess
loaddata_command = f"python manage.py loaddata {json_filename}"
subprocess.call(loaddata_command, shell=True)
print(f"Fixture data has been saved to {json_file_path}")