#!/bin/sh

echo "Waiting for DB..."

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo "PostgreSQL DB"



python manage.py makemigrations --noinput
python manage.py migrate --noinput
#python manage.py collectstatic  --noinput
#python manage.py createsuperuser --noinput --username samoore
gunicorn -c /var/tmp/conf.py app.wsgi:application

