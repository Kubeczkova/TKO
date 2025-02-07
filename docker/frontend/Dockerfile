ARG NODE_VERSION=22

FROM node:${NODE_VERSION}-slim AS base

USER node

WORKDIR /app

FROM base AS dev

ARG UID=1000
ARG GID=1000

USER root

RUN usermod -u ${UID} node && groupmod -g ${GID} node

WORKDIR /app
USER node

CMD [ "npm", "run", "dev" ]

FROM base AS deps

WORKDIR /app

COPY services/frontend/package*.json ./

RUN : \
    && npm ci \
    && :

COPY services/frontend ./

RUN : \
    && npm run build \
    && :

FROM node:${NODE_VERSION}-slim AS release

WORKDIR /app
COPY --from=deps /app/.output ./.output

CMD [ "node", ".output/server/index.mjs" ]