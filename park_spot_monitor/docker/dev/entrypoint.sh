#!/bin/sh
set -e

echo "Container's IP address: `awk 'END{print $1}' /etc/hosts`"
echo "Waiting for PostgreSQL to start..."
./wait-for-it.sh postgres:5432 --timeout=30
echo "PostgreSQL has started"


# if [ "$1" = 'server' ]; then
#     sh examples/server/$@ -bi
# else
#     if [ "$1" = 'client' ]; then
#         sh examples/client/$@
#     else
#         exec "$@"
#     fi
# fi