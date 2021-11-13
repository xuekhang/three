release: python manage.py migrate --noinput
web: daphne -b 0.0.0.0 -p 8000 three.asgi:application