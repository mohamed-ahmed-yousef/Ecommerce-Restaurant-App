import json
import os
# from django.contrib.auth import get_user_model

# CustomUser = get_user_model()

users_data = [
    {
        "model": "accounts.customuser",
        "pk": 1,
        "fields": {
            "email": "user1@example.com",
            "name": "User 1",
            "email_confirmed": True,
            "profile_completed": True
        }
    },
    {
        "model": "accounts.customuser",
        "pk": 2,
        "fields": {
            "email": "user2@example.com",
            "name": "User 2",
            "email_confirmed": False,
            "profile_completed": False
        }
    }
]
profiles_data = [
    {
        "model": "accounts.profile",
        "pk": 1,
        "fields": {
            "user": 1,  # Corresponds to the pk of user with email "user1@example.com"
            "bio": "User 1's bio.",
            "profile_image": "path/to/user1_profile_image.jpg",  # Replace with actual image path
            "date_of_birth": "1990-01-01",
            "street": "Street 1",
            "house": "House 1",
            "floor": "Floor 1",
            "phone_number": "1234567890"
        }
    },
    {
        "model": "accounts.profile",
        "pk": 2,
        "fields": {
            "user": 2,  # Corresponds to the pk of user with email "user2@example.com"
            "bio": "User 2's bio.",
            "profile_image": "path/to/user2_profile_image.jpg",  # Replace with actual image path
            "date_of_birth": "1995-05-05",
            "street": "Street 2",
            "house": "House 2",
            "floor": "Floor 2",
            "phone_number": "9876543210"
        }
    }
]

fixture_data = users_data + profiles_data
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









































