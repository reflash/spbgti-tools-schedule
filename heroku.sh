#!/usr/bin/env bash
# Change this when it will come for real production
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell
python manage.py migrate api
python manage.py migrate core