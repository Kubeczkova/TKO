# Template project

## Running

1. create .env from .env.example 
2. `docker compose run --rm frontend npm install`
3. `docker compose build`
4. `docker compose up`

## Adding new frontend packages

`docker compose run --rm frontend npm install <package>`

## Adding new backend packages

`docker compose run --rm backend uv add <package>`