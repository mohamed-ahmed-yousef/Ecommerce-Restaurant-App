#!/bin/bash
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser( 'admin@gmail.com', 'password')" | python manage.py shell
echo "create super user successful"