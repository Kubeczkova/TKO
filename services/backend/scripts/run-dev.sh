#!/usr/bin/env bash
set -euxo pipefail

python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000