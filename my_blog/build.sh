#!/usr/bin/env bash
# Install dependencies


# Logging
echo "Current directory: $(pwd)"
echo "Installing dependencies from requirements.txt"
pip install -r requirements.txt

echo "Current directory: $(pwd)"
echo "loacating collectstatic from manage.py"

python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"