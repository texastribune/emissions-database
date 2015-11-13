#!/bin/bash

# Migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run app
exec gunicorn emission_events.wsgi:application \
  --workers 3 \
  --bind 0.0.0.0:8000 \
  "$@"
