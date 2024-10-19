#!/usr/bin/env bash
# Install dependencies
set -e
cd $(dirname "$0")  # Navigate to the directory where build.sh is located

# Logging the current directory
echo "Current directory: $(pwd)"

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Found requirements.txt. Installing dependencies..."
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

# Check if manage.py exists in the current directory
if [ -f "manage.py" ]; then
    echo "Found manage.py. Proceeding with collectstatic and migrations..."
else
    echo "Error: manage.py not found in the current directory!"
    exit 1
fi

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Create superuser if required
if [[ $CREATE_SUPERUSER ]]; then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
