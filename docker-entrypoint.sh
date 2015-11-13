#!/bin/bash

# Migrations
python emission_events/manage.py migrate

# Collect static files
python emission_events/manage.py collectstatic --noinput

# Run app
exec gunicorn emission_events.emission_events.wsgi:application \
  --workers 3 \
  --bind 0.0.0.0:8000 \
  "$@"