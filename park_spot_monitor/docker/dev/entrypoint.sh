#!/bin/sh
set -e

echo "Container's IP address: `awk 'END{print $1}' /etc/hosts`"
echo "Waiting for PostgreSQL to start..."
./wait-for-it.sh postgres:5432 --timeout=30
echo "PostgreSQL has started"
poetry run python manage.py migrate
exec "$@"
