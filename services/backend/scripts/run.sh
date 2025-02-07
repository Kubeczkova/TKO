#!/usr/bin/env bash
set -euxo pipefail

uvicorn \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    backend.asgi:application