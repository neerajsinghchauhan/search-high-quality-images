#!/usr/bin/env bash
# Install dependencies
set -e
cd $(dirname "$0")

# Logging
echo "Current directory: $(pwd)"
echo "Installing dependencies from requirements.txt"


pip install -r requirements.txt


# Collect static files
set -e
cd $(dirname "$0")

# Logging
echo "Current directory: $(pwd)"
echo "loacating collectstatic from manage.py"

python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"