# from decimal import Decimal
import json
import os
import uuid
# from django.contrib.auth import get_user_model
from random import choices

# from django.utils import timezone

# CustomUser = get_user_model()
delivery_choices = (
    ('delivery', 'delivery'),
    ('takeaway', 'takeaway'),
)

orders_data = [
    {
        "model": "orders.order",
        "pk": 1,
        "fields": {
            "delivery_option": choices(delivery_choices)[0][0],
            "time_preferred":'2021-01-01T00:00:00Z',
            "customer": 1,  # Replace with the ID of the CustomUser who placed the order
            "restaurant": 1,  # Replace with the ID of the Restaurant associated with the order
            "total_price": 50.00 , # Replace with the actual total price of the order
        }
    },
    # Add more orders as needed...
]

# Generate data for OrderItem
order_items_data = [
    {
        "model": "orders.orderitem",
        "pk": 1,
        "fields": {
             "item":1, # Corresponds to the ID of the first order in orders_data
            "quantity": 2,  # Replace with the actual quantity of this order item
            'order': 1
        }
    },
    # Add more order items as needed...
]

# Generate data for DeliveryCharge
# delivery_charges_data = [
#     {
#         "model": "orders.deliverycharge",
#         "pk": 1,
#         "fields": {
#             "region": "Region 1",  # Replace with the region name
#             "charge":5.00  # Replace with the actual delivery charge for this region
#         }
#     },
#     # Add more delivery charges as needed...
# ]
fixture_data =   order_items_data+orders_data
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









































