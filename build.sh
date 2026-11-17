#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create the demo admin only once so later deploys do not reset its password.
python -c "
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MobileMoney.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists; leaving its credentials unchanged')
"