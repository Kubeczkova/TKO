#!/usr/bin/env bash

set -euxo pipefail

wait-for-it \
--quiet \
--service ${DATABASE_HOST}:${DATABASE_PORT:-5432} \
--timeout 60 \
-- echo "db is up"

exec "$@";