# Template project

## Running

1. `docker compose run --rm frontend npm install`
2. `docker compose build`
3. `docker compose up`

## Adding new frontend packages

`docker compose run --rm frontend npm install <package>`

## Adding new backend packages

`docker compose run --rm backend uv add <package>`