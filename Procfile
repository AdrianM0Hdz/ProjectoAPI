web: gunicorn game_api.wsgi:application
release: python manage.py makemigrations --noinput 
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput