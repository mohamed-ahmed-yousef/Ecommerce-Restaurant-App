import os
import uuid

restaurants_data = [
    {
        "model": "restaurants.restaurant",
        "pk":1,
        "fields": {
            "name": "Restaurant 1",
            "location": "Location 1",
            "house": "House 1",
            "road": "Road 1",
            "city": "City 1",
            "delivery_time": "30 minutes",
            "min_order": 10,
            "rate": 4,
            "image": "path/to/restaurant1_image.jpg"  # Replace with actual image path
        }
    },
    {
        "model": "restaurants.restaurant",
        "pk": 2,
        "fields": {
            "name": "Restaurant 2",
            "location": "Location 2",
            "house": "House 2",
            "road": "Road 2",
            "city": "City 2",
            "delivery_time": "45 minutes",
            "min_order": 20,
            "rate": 5,
            "image": "path/to/restaurant2_image.jpg"  # Replace with actual image path
        }
    },
    {
        "model": "restaurants.restaurant",
        "pk": 2,
        "fields": {
            "name": "Restaurant 3",
            "location": "Location 3",
            "house": "House 3",
            "road": "Road 3",
            "city": "City 3",
            "delivery_time": "20 minutes",
            "min_order": 15,
            "rate": 3,
            "image": "path/to/restaurant3_image.jpg"  # Replace with actual image path
        }
    }
]
campaigns_data = [
    {
        "model": "restaurants.campaign",
        "pk": 1,
        "fields": {
            "name": "Campaign 1",
            "start_date": "2023-07-01",
            "end_date": "2023-07-15",
            "description": "Campaign 1 description.",
            "image": "path/to/campaign1_image.jpg",  # Replace with actual image path
            "restaurant":'1' # Restaurant 1 and Restaurant 2
        }
    },
    {
        "model": "restaurants.campaign",
        "pk": 2,
        "fields": {
            "name": "Campaign 2",
            "start_date": "2023-08-01",
            "end_date": "2023-08-31",
            "description": "Campaign 2 description.",
            "image": "path/to/campaign2_image.jpg",  # Replace with actual image path
            "restaurant":'2' # Restaurant 2 and Restaurant 3
        }
    }
]
import json

fixture_data = restaurants_data + campaigns_data

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