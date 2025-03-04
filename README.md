# three

Deployed to scattergo.com


need to update redis and postgres local settings to run locally. current settings are for heroku.

# Getting Started
1. Run `docker compose up`
2. Run `python manage.py migrate`
3. Run `python manage.py loaddata game/fixtures/initial_data.json`
4. Run `daphne three.asgi:application`

## Seed inital categories data
