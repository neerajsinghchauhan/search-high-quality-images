#!/usr/bin/env bash
# Install dependencies
set -e

# Move to the directory where requirements.txt is located
cd $(dirname "$0")

# Logging
echo "Current directory: $(pwd)"
echo "Installing dependencies from requirements.txt"
pip install -r requirements.txt

# Move to the directory where manage.py is located (up one level)
cd ..

# Logging
echo "Moved to directory: $(pwd)"
echo "Running collectstatic from manage.py"

# Run collectstatic and migrations
python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser if the CREATE_SUPERUSER environment variable is set
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
