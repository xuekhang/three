# three

## Getting Started
1. Run `docker compose up`
2. Run:
    * `docker exec -it daphne bash`
    * `python manage.py migrate`

## Seed inital categories data
1. Run `python manage.py loaddata game/fixtures/initial_data.json`