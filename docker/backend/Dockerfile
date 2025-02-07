ARG PYTHON_VERSION=3.13
ARG POSTGRES_VERSION=17

FROM python:${PYTHON_VERSION}-slim AS base


ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    DEBIAN_FRONTEND=noninteractive

RUN : \
    && apt-get update \
    && apt-get install -y \
        build-essential \
        openssh-client \
        gnupg \
        wget \
        lsb-release \
        git \
    && rm -rf /var/lib/apt/lists* \
    && :

RUN : \
    && echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt update \
    && apt install -y postgresql-client-${POSTGRESQL_VERSION} libpq-dev \
    && rm -rf /var/lib/apt/lists* \
    && :

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

FROM base AS deps

RUN adduser --disabled-password runner

USER runner

WORKDIR /app

# COPY services/backend/pyproject.toml services/backend/uv.lock ./

ENV UV_PROJECT_ENVIRONMENT=/home/runner/.venv \
    UV_PYTHON_DOWNLOADS=never

RUN --mount=type=bind,target=/app,source=./services/backend \
    : \
    && uv sync --frozen \
    && :

ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]

FROM deps AS dev

ARG UID=1000
ARG GID=1000

USER root

RUN usermod -u ${UID} runner && groupmod -g ${GID} runner

ENV PATH=${UV_PROJECT_ENVIRONMENT}/bin:${PATH}

WORKDIR /app
USER runner

CMD [ "/app/scripts/run-dev.sh" ]

FROM deps AS release

ENV PATH=${UV_PROJECT_ENVIRONMENT}/bin:${PATH}

WORKDIR /app
COPY --chown=runner:runner services/backend/ ./

CMD [ "/app/scripts/run.sh" ]
